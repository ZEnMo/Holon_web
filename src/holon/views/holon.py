import json
import traceback

from django.apps import apps
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from sentry_sdk import capture_exception

from holon.cache import holon_endpoint_cache
from holon.models import Scenario
from holon.rule_engine import rule_mapping
from holon.models.config import QueryCovertModuleType
from holon.models.scenario_rule import ModelType, DatamodelQueryRule
from holon.models.util import all_subclasses, is_exclude_field
from holon.serializers import HolonRequestSerializer
from holon.services import CostTables, ETMConnect
from holon.services.cloudclient import CloudClient
from holon.services.cloudclient.input import inputs_to_debug_values
from holon.services.cloudclient.output import AnyLogicOutput
from holon.services.data import Results
from holon.utils.logging import HolonLogger
from holon.rule_engine.scenario_aggregate import ScenarioAggregate


def use_result_cache(request: Request) -> bool:
    """
    Caching simulation results is enabled by default unless cookie or query param is set.
    Set cookie in javascript console:
    document.cookie = "caching=false; Path=/; SameSite=none; domain=holons.energy; secure"
    """
    if request.query_params.get("caching", "true").lower() == "false":
        return False

    if request.COOKIES.get("caching", "true").lower() == "false":
        return False

    return True


def default_etm_outcomes():
    return {
        "cost_outcome": None,
        "nat_upscaling_outcomes": None,
        "inter_upscaling_outcomes": None,
        "depreciation_costs": [],
    }


class HolonV2Service(generics.CreateAPIView):
    logger = HolonLogger("holon-endpoint")
    serializer_class = HolonRequestSerializer

    def post(self, request: Request):
        serializer = HolonRequestSerializer(data=request.data)

        use_caching = use_result_cache(request)
        scenario: Scenario | None = None
        anylogic_output: AnyLogicOutput | None = None
        debug_values = {
            "scenario": {},
            "anylogic": {
                "input": {},
                "output": {},
            },
        }

        try:
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            data = serializer.validated_data
            scenario_id = data["scenario"]
            interactive_elements = serializer.create_interactive_elements()

            cache_key: None | str = None
            if use_caching:
                cache_key = holon_endpoint_cache.generate_key(scenario_id, interactive_elements)

                value = holon_endpoint_cache.get(cache_key)

                if value:
                    HolonV2Service.logger.log_print(f"HOLON cache hit on: {cache_key}")
                    return Response(
                        value,
                        status=status.HTTP_200_OK,
                    )

            # RULE ENGINE - APPLY INTERACTIVE ELEMENTS
            HolonV2Service.logger.log_print("Applying interactive elements to scenario")

            scenario = Scenario.queryset_with_relations().get(id=scenario_id)
            debug_values["scenario"] = {
                "id": scenario.id,
                "name": scenario.name,
            }

            scenario_aggregate = ScenarioAggregate(scenario)
            scenario_aggregate = rule_mapping.apply_rules(scenario_aggregate, interactive_elements)

            # RUN ANYLOGIC
            HolonV2Service.logger.log_print("Running Anylogic model")
            anylogic_client = CloudClient(payload=scenario_aggregate, scenario=scenario)
            debug_values["anylogic"]["input"] = {
                # TODO: this is quite computationally expensive, see if we can do it only when needed
                "debug": inputs_to_debug_values(anylogic_client.create_inputs())
            }
            anylogic_output = anylogic_client.run()
            # Disabled because it makes the response too big for common tooling
            # debug_values["anylogic"]["output"] = {
            #     # TODO: this is quite computationally expensive, see if we can do it only when needed
            #     "debug": anylogic_output.get_debug_output(),
            #     # It would be useful to include the interpreted values but the response is getting too big
            #     # "decoded": anylogic_output.decoded,
            # }

            # ETM Module
            # We want to be resilient in the face of errors.
            # When the ETM module fails, we return the results of the AnyLogic part.
            etm_outcomes = default_etm_outcomes()
            error = None
            try:
                HolonV2Service.logger.log_print("Running ETM module")
                etm_outcomes = self._etm_results(scenario, scenario_aggregate, anylogic_output)
            except Exception as e:
                error = e
                traceback.print_exception(e)
                capture_exception(e)

            HolonV2Service.logger.log_print("Calculating CostTables")
            cost_benefit_tables = self._cost_benefit_tables(
                etm_outcomes.pop("depreciation_costs"), scenario_aggregate, anylogic_output
            )

            results = Results(
                debug_values=debug_values,
                request=request,
                anylogic_outcomes=anylogic_output,
                cost_benefit_overview=cost_benefit_tables.main_table(),
                cost_benefit_detail=cost_benefit_tables.all_detailed_tables(),
                **etm_outcomes,
                anylogic_outputs=anylogic_output.create_dict(data["anylogic_output_keys"]),
                datamodel_query_results=DatamodelQueryRule.execute_multiple(
                    data["datamodel_query_rules"], scenario_aggregate
                ),
                error=error,
            )

            HolonV2Service.logger.log_print("200 OK")

            result = results.to_dict()

            if use_caching:
                holon_endpoint_cache.set(cache_key, result)

            return Response(
                result,
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            traceback.print_exc()
            capture_exception(e)

            response_body = {
                "error_msg": f"something went wrong: {e}",
                "debug_values": debug_values,
            }

            return Response(
                response_body,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def _etm_results(
        self,
        scenario: Scenario,
        scenario_aggregate: ScenarioAggregate,
        anylogic_output: AnyLogicOutput,
    ):
        """Returns a dict with results from the ETM"""
        etm_outcomes = default_etm_outcomes()

        for module, outcome in ETMConnect.connect_from_scenario(
            scenario, scenario_aggregate, anylogic_output.decoded
        ):
            if module == QueryCovertModuleType.COST:
                etm_outcomes["cost_outcome"] = outcome
            elif module == QueryCovertModuleType.UPSCALING:
                etm_outcomes["nat_upscaling_outcomes"] = outcome
            elif module == QueryCovertModuleType.UPSCALING_REGIONAL:
                etm_outcomes["inter_upscaling_outcomes"] = outcome
            elif module == QueryCovertModuleType.COSTBENEFIT:
                etm_outcomes["depreciation_costs"] = outcome
            else:
                raise Exception(f"Unknow ETM module {module}")

        return etm_outcomes

    def _cost_benefit_tables(
        self,
        depreciation_costs,
        scenario_aggregate: ScenarioAggregate,
        anylogic_output: AnyLogicOutput,
    ) -> CostTables:
        tables = CostTables.from_al_output(
            self._find_contracts(anylogic_output), scenario_aggregate
        )
        for costs in depreciation_costs:
            tables.inject_depreciation_costs(costs)
        return tables

    def _find_contracts(self, anylogic_output: AnyLogicOutput):
        """Finds contracts in the AnyLogic outcomes, needed for cost tables"""
        try:
            return anylogic_output.decoded["contract_data"]
        except KeyError as err:
            HolonV2Service.logger.log_print(
                "Contract data is not mapped, trying to find the correct output..."
            )
            key = anylogic_output.source.find_name_including("contract")
            return json.loads(anylogic_output.source.value(key))


class HolonCacheCheck(generics.CreateAPIView):
    logger = HolonLogger("holon-cache-check")
    serializer_class = HolonRequestSerializer

    def post(self, request: Request):
        if not use_result_cache(request):
            # This gives the right experience in the frontend
            return Response(
                {"is_cached": False},
                status=status.HTTP_200_OK,
            )

        serializer = HolonRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        cache_key = holon_endpoint_cache.generate_key(
            data["scenario"], serializer.create_interactive_elements()
        )
        key_exists = holon_endpoint_cache.exists(cache_key)

        return Response(
            {"is_cached": key_exists},
            status=status.HTTP_200_OK,
        )


class HolonCMSLogic(generics.RetrieveAPIView):
    valid_relations = [apps.get_model("holon", model[0]) for model in ModelType.choices]

    def get(self, request):
        response = {}

        for model in ModelType.choices:
            model_name = model[0]
            model_type_class = apps.get_model("holon", model_name)

            attributes = self.get_attributes_and_relations(model_type_class)

            response[model_name] = {
                "attributes": attributes,
                "model_subtype": {},
            }

            for subclass in all_subclasses(model_type_class):
                response[model_name]["model_subtype"][subclass.__name__] = (
                    self.get_attributes_and_relations(subclass)
                )

        return Response(response)

    def get_attributes_and_relations(self, model_type_class):
        attributes = []

        for field in model_type_class()._meta.get_fields():
            if is_exclude_field(field):
                continue
            attribute = {"name": field.name}
            if field.is_relation and issubclass(field.related_model, tuple(self.valid_relations)):
                attribute["relation"] = field.related_model.__name__
            attributes.append(attribute)
        return attributes


def holonCMSLogicFormatter(request):
    configs = HolonCMSLogic().get(request)
    return render(request, "modelconfig.html", {"configs": configs.data})


class HolonScenarioCleanup(generics.RetrieveAPIView):
    logger = HolonLogger("holon-scenario-cleanup")

    def get(self, request):
        cloned_scenarios = Scenario.objects.filter(cloned_from__isnull=False)
        try:
            for scenario in cloned_scenarios:
                HolonScenarioCleanup.logger.log_print(f"Deleting scenario {scenario.id}...")
                cid = scenario.id
                scenario.delete()
                HolonScenarioCleanup.logger.log_print(f"... deleted scenario {cid}")
        except Exception as e:
            HolonScenarioCleanup.logger.log_print(traceback.format_exc())
            response_body = {"error_msg": f"something went wrong: {e}"}
            return Response(
                response_body,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response("succes")


class HolonService(generics.CreateAPIView):
    def post(self, request):
        return Response(
            "This endpoint is no longer in use, upgrade to the new endpoin!",
            status=status.HTTP_410_GONE,
        )

from django.test import TestCase
import pytest

from holon.models import *
from holon.models import rule_mapping
from holon.rule_engine.scenario_aggregate import ScenarioAggregate
from holon.models.scenario_rule import ModelType


class ScenarioAggregateRemoveTestClass(TestCase):
    def setUp(self) -> None:
        self.scenario: Scenario = Scenario.objects.create(name="test")
        self.actor0: Actor = Actor.objects.create(
            category=ActorType.CONNECTIONOWNER, payload=self.scenario
        )
        self.actor1: Actor = Actor.objects.create(
            category=ActorType.CONNECTIONOWNER, payload=self.scenario
        )
        self.actor2: Actor = Actor.objects.create(
            category=ActorType.CONNECTIONOWNER, payload=self.scenario
        )
        self.gridconnection_0: BuildingGridConnection = BuildingGridConnection.objects.create(
            owner_actor=self.actor1,
            capacity_kw=750.0,
            payload=self.scenario,
            insulation_label=InsulationLabel.A,
            heating_type=HeatingType.GASBURNER,
            type=BuildingType.LOGISTICS,
        )
        self.gridconnection_1: BuildingGridConnection = BuildingGridConnection.objects.create(
            owner_actor=self.actor1,
            capacity_kw=750.0,
            payload=self.scenario,
            insulation_label=InsulationLabel.A,
            heating_type=HeatingType.GASBURNER,
            type=BuildingType.LOGISTICS,
        )
        self.gridconnection_2: BuildingGridConnection = BuildingGridConnection.objects.create(
            owner_actor=self.actor2,
            capacity_kw=750.0,
            payload=self.scenario,
            insulation_label=InsulationLabel.A,
            heating_type=HeatingType.GASBURNER,
            type=BuildingType.LOGISTICS,
        )
        self.asset1 = ElectricHeatConversionAsset.objects.create(
            gridconnection=self.gridconnection_0,
            name="building_heat_pump",
            type=ConversionAssetType.HEAT_PUMP_AIR,
            eta_r=0.95,
            deliveryTemp_degC=70.0,
            capacityElectricity_kW=30.0,
        )
        self.asset2 = ElectricHeatConversionAsset.objects.create(
            gridconnection=self.gridconnection_0,
            name="building_heat_pump",
            type=ConversionAssetType.HEAT_PUMP_AIR,
            eta_r=0.95,
            deliveryTemp_degC=70.0,
            capacityElectricity_kW=30.0,
        )
        self.asset3 = ElectricHeatConversionAsset.objects.create(
            gridconnection=self.gridconnection_1,
            name="building_heat_pump",
            type=ConversionAssetType.HEAT_PUMP_AIR,
            eta_r=0.95,
            deliveryTemp_degC=70.0,
            capacityElectricity_kW=30.0,
        )
        self.asset4 = ElectricHeatConversionAsset.objects.create(
            gridconnection=self.gridconnection_2,
            name="building_heat_pump",
            type=ConversionAssetType.HEAT_PUMP_AIR,
            eta_r=0.95,
            deliveryTemp_degC=70.0,
            capacityElectricity_kW=30.0,
        )

        self.scenario_aggregate = ScenarioAggregate(self.scenario)

    def test_remove_assets(self):
        self.scenario_aggregate.remove_object(self.asset3)
        assert self.scenario_aggregate.repositories[ModelType.ENERGYASSET.value].len() == 3
        self.scenario_aggregate.remove_object(self.asset1)
        assert self.scenario_aggregate.repositories[ModelType.ENERGYASSET.value].len() == 2
        self.scenario_aggregate.remove_object(self.asset2)
        assert self.scenario_aggregate.repositories[ModelType.ENERGYASSET.value].len() == 1
        self.scenario_aggregate.remove_object(self.asset4)
        assert self.scenario_aggregate.repositories[ModelType.ENERGYASSET.value].len() == 0

        self.assertRaises(
            ValueError,
            self.scenario_aggregate.remove_object,
            self.asset4,
        )

    def test_remove_actors_cascade(self):
        self.scenario_aggregate.remove_object(self.actor0)
        assert self.scenario_aggregate.repositories[ModelType.ACTOR.value].len() == 2

        # check if gridconnection0 is deleted according to the CASCADE rule
        assert self.scenario_aggregate.repositories[ModelType.GRIDCONNECTION.value].len() == 2

        # check if asset1 and asset2 are deleted according to the CASCADE rule
        assert self.scenario_aggregate.repositories[ModelType.ENERGYASSET.value].len() == 2

    # def test_remove_gridconnections(self):
    #     self.scenario_aggregate.remove_object(self.gridconnection_0)
    #     assert len(self.scenario_aggregate.repositories[ModelType.ACTOR.value].all()) == 2
    #     self.scenario_aggregate.remove_object(self.actor1)
    #     assert len(self.scenario_aggregate.repositories[ModelType.ACTOR.value].all()) == 1
    #     self.scenario_aggregate.remove_object(self.actor2)
    #     assert len(self.scenario_aggregate.repositories[ModelType.ACTOR.value].all()) == 0

    #     self.assertRaises(
    #         ValueError,
    #         self.scenario_aggregate.remove_object,
    #         self.actor1,
    #     )

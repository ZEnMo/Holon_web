from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from holon.rule_engine.scenario_aggregate import ScenarioAggregate
    from holon.rule_engine.repositories.repository_base import RepositoryBaseClass

from holon.models.rule_actions import RuleAction
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from holon.models.scenario_rule import ScenarioRule
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel


from holon.models.util import is_allowed_relation


class ChangeAttributeOperator(models.TextChoices):
    """Types of supported mathematical operators"""

    SET = "="
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


class RuleActionChangeAttribute(RuleAction, ClusterableModel):
    """A discrete factor for setting the value of an attribute"""

    model_attribute = models.CharField(max_length=255, null=False)
    operator = models.CharField(max_length=255, choices=ChangeAttributeOperator.choices)
    static_value = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel("model_attribute"),
        FieldPanel("operator"),
        FieldPanel("static_value"),
        InlinePanel(
            "rule_action_conversion_step",
            heading="Queried value",
            label="Conversion stap",
            min_num=0,
            max_num=1,
        ),
    ]
    rule: ScenarioRule = ParentalKey(
        ScenarioRule, on_delete=models.CASCADE, related_name="discrete_factors_change_attribute"
    )

    class Meta:
        verbose_name = "RuleActionChangeAttribute"

    def clean(self):
        super().clean()

        try:
            if not self.model_attribute in self.rule.get_model_attributes_options():
                raise ValidationError(f"Invalid value {self.model_attribute} for model_attribute")
        except ObjectDoesNotExist:
            return

    def hash(self):
        return f"[A{self.id},{self.model_attribute},{self.operator},{self.static_value}]"

    def __apply_operator(self, value_old, input_value):
        """Cast the input value to the same type of the old value and apply the chosen operator"""

        # return input value if set
        if self.operator == ChangeAttributeOperator.SET:
            return input_value

        # cast to float to make all operators work as expected
        val_a_flt = float(value_old)
        val_b_flt = float(input_value)

        # apply operator
        if self.operator == ChangeAttributeOperator.ADD:
            return val_a_flt + val_b_flt
        if self.operator == ChangeAttributeOperator.SUBTRACT:
            return val_a_flt - val_b_flt
        if self.operator == ChangeAttributeOperator.MULTIPLY:
            return val_a_flt * val_b_flt
        if self.operator == ChangeAttributeOperator.DIVIDE:
            return val_a_flt / val_b_flt

    def apply_to_scenario_aggregate(
        self,
        scenario_aggregate: ScenarioAggregate,
        filtered_repository: RepositoryBaseClass,
        value: str,
        number_generator: random.Random,
    ) -> ScenarioAggregate:
        """Apply a rule action to an object in the repository"""

        if self.static_value:
            value = self.static_value

        conversion_step = self.rule_action_conversion_step.first()
        if conversion_step:
            value = conversion_step.get_value(scenario_aggregate)

        model_attribute = self.model_attribute
        if is_allowed_relation(model_attribute):
            # Add id to attribute so it can be updated with an id compared to a model instance
            model_attribute += "_id"
            if value is not None:
                if value.lower() == "none" or value.lower() == "null":
                    value = None
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        raise ValueError(
                            f"{model_attribute} must be an integer or None, got {repr(value)}"
                        )

        # apply operators to objects
        for filtered_object in filtered_repository.all():
            old_value = getattr(filtered_object, model_attribute)
            new_value = self.__apply_operator(old_value, value)

            # change the new value type to the same as the old one
            try:
                cast_new_value = type(old_value)(new_value)
            except:
                # fallback when old_value is None
                cast_new_value = new_value

            # update scenario aggregate
            setattr(filtered_object, model_attribute, cast_new_value)
            scenario_aggregate.repositories[filtered_repository.base_model_type.__name__].update(
                filtered_object
            )

        return scenario_aggregate

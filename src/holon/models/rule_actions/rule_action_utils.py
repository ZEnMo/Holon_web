from polymorphic import utils

from holon.models.actor import Actor
from holon.models.asset import EnergyAsset
from holon.models.contract import Contract
from holon.models.gridconnection import GridConnection
from holon.models.gridnode import GridNode
        
class RuleActionUtils:
    """ A collection of util functions for rule actions """ 

    def get_parent_classes_and_field_names(model_type: type) -> list[tuple[type, str]]:
        """
        Get the class type(s) and field name(s) of the foreign key fields of the class type.
        """

        base_class = utils.get_base_polymorphic_model(model_type)

        if base_class == EnergyAsset:
            return [(GridConnection, "gridconnection"), (GridNode, "gridnode")]

        if base_class == GridConnection:
            return [(Actor, "owner_actor")]

        if base_class == Contract:
            return [(Actor, "owner_actor")]
"""Create a Costs&Benefits Table """
from holon.models import Actor


class CostTables:
    def __init__(self, cost_items: list) -> None:
        """cost_items is a list of CostItems, we now loop it a lot - can that be improved?"""
        self.cost_items = cost_items

    def main_table(self) -> dict:
        return CostTable(self.cost_items).table

    def detailed_table(self, group) -> dict:
        return CostTable(self.cost_items, use_subgroup=group).table

    def groups_for_detailed(self) -> set:
        return set((group for item in self.cost_items for group in item.with_subgroups()))

    def all_detailed_tables(self) -> dict:
        """
        Returns a dict where the keys are the applicable actor groups
        and the values are their detailed tables
        """
        return {group: self.detailed_table(group) for group in self.groups_for_detailed()}

    @classmethod
    def from_al_output(cls, al_output, scenario):
        actors = ActorWrapper.from_scenario(scenario)
        return cls([CostItem.from_dict(item, actors) for item in al_output])


class CostTable:
    def __init__(self, cost_items, use_subgroup=None) -> None:
        """cost_items is a list of CostItems"""
        self._use_subgroup = use_subgroup
        self.table = cost_items

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, cost_items):
        self._table = {}
        for item in cost_items:
            self.__add_to_table(item)
            self.__add_to_table(CostItem.reversed(item))
        self.__fill_out_table()
        self.__round_table()

    def __add_to_table(self, item):
        """Adds the item to the table"""
        try:
            self._table[self.__name_from(item)][self.__name_to(item)] += item.price
        except:
            self.__add_to_group(item)

    def __add_to_group(self, item):
        try:
            self._table[self.__name_from(item)][self.__name_to(item)] = item.price
        except KeyError:
            self.__add_from_group(item)

    def __add_from_group(self, item):
        """
        Also needs to add self as None
        TODO: move some functionality from fill_out_table here
        """
        self._table[self.__name_from(item)] = {
            self.__name_to(item): item.price,
            self.__name_from(item): 0.0,
        }

    def __fill_out_table(self):
        # we can also keep a global set in memory (self) where we add to in __add_from_group
        all_groups = set((key for value in self.table.values() for key in value.keys()))
        basic = {key: 0.0 for key in all_groups}
        for group in all_groups:
            self._table[group] = basic | self._table.get(group, {})
            self._table[group]["Netto kosten"] = sum(
                (value for value in self._table[group].values() if value is not None)
            )

    def __round_table(self):
        """loops through the final table and rounds all values"""

        for holder, transactions in self._table.items():
            try:
                for scope, transaction in transactions.items():
                    self._table[holder][scope] = int(transaction)
            except TypeError:  # unsure if we ever get deeper, but just to be sure
                for deeper_scope, deeper_transaction in transaction.items():
                    self._table[holder][scope][deeper_scope] = int(deeper_transaction)

    def __name_from(self, item):
        return (
            item.from_subgroup() if self._use_subgroup == item.from_group() else item.from_group()
        )

    def __name_to(self, item):
        return item.to_subgroup() if self._use_subgroup == item.to_group() else item.to_group()


class ActorWrapper:
    def __init__(self, id_to_actor: dict[int, Actor]) -> None:
        """Where actors is the Django equivalent of AR relation of Actors of the scenario"""
        self.id_to_actor = id_to_actor

    def find(self, actor_name):
        """
        Strips the AL prefix from the actor name and returns the corresponding Actor
        """
        return self.id_to_actor[int(actor_name[3:])]

    @classmethod
    def from_scenario(cls, scenario):
        # In scenario "Transitie Visie Warmte"
        # doing this eagerly prevents many thousands of queries
        # even though there are only 44 actors.
        actors = list(
            scenario.actor_set.all().prefetch_related("group").prefetch_related("subgroup")
        )
        id_to_actor: dict[int, Actor] = {actor.id: actor for actor in actors}

        return cls(id_to_actor)


class CostItem:
    """Represents one contract in the AL output"""

    def __init__(self, to_actor, from_actor, price) -> None:
        self.from_actor = from_actor
        self.to_actor = to_actor
        self.price = price

    def from_group(self):
        return CostItem.group(self.from_actor)

    def to_group(self):
        return CostItem.group(self.to_actor)

    def from_subgroup(self):
        return CostItem.subgroup(self.from_actor)

    def to_subgroup(self):
        return CostItem.subgroup(self.to_actor)

    def with_subgroups(self):
        """Returns groups that are connected to a subgroup"""
        if self.from_actor.subgroup:
            yield self.from_group()
        if self.to_actor.subgroup:
            yield self.to_group()

    @staticmethod
    def group(actor):
        """Fallback to category if group is not defined"""
        try:
            return actor.group.name
        except AttributeError:
            return actor.category

    @staticmethod
    def subgroup(actor):
        """Fallback to group if subgroup is not defined"""
        try:
            return f"{CostItem.group(actor)} - {actor.subgroup.name}"
        except AttributeError:
            return CostItem.group(actor)

    @staticmethod
    def price_for(obj) -> float:
        """
        FinancialTransactionVolume_eur includes all contract cost:
            1. Energycarrier_volume x Energycarrier_price
            2. Annual_fee
            3. Taxes
               -> All parameters are determined in AnyLogic

        Defaults to 0.0
        """
        return -obj.get("FinancialTransactionVolume_eur", 0.0)
        # should be negative because costs are negative in frontend
        # but positive output from Anylogic

    @staticmethod
    def delivery_or_feedin_price(obj) -> float:
        """Redundant function: Check for the delivery price. If no prices sets defaults to 0"""
        volume = obj.get("EnergyTransactionVolume_kWh", 0.0)
        if volume > 0:
            return volume * (
                obj.get("feedinTax_eurpkWh", 0.0) + obj.get("feedinPrice_eurpkWh", 0.0)
            )
        return volume * (
            obj.get("deliveryTax_eurpkWh", 0.0) + obj.get("deliveryPrice_eurpkWh", 0.0)
        )

    @classmethod
    def from_dict(cls, obj: dict, actors: ActorWrapper):
        return cls(
            from_actor=actors.find(obj["contractHolder"]),
            to_actor=actors.find(obj["contractScope"]),
            price=CostItem.price_for(obj),
        )

    @classmethod
    def reversed(cls, obj: "CostItem"):
        """Takes a CostItem returns a new CostItem with the from and to actors switched and the price negated"""
        return cls(
            to_actor=obj.from_actor,
            from_actor=obj.to_actor,
            price=-obj.price,
        )

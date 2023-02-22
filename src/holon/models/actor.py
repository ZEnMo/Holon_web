from django.db import models

from holon.models.scenario import Scenario
from polymorphic.models import PolymorphicModel


class ActorType(models.TextChoices):
    OPERATORGRID = "OPERATORGRID"
    GOVHOLON = "GOVHOLON"
    HOLONENERGY = "HOLONENERGY"
    CONNECTIONOWNER = "CONNECTIONOWNER"
    SUPPLIERENERGY = "SUPPLIERENERGY"


class Group(models.TextChoices):
    COMMERCIAL = "COMMERCIAL"
    HOUSEHOLD = "HOUSEHOLD"


class SubGroup(models.TextChoices):
    RICH = "RICH"
    POOR = "POOR"
    REGULAR = "REGULAR"


class Actor(PolymorphicModel):
    category = models.CharField(max_length=255, choices=ActorType.choices)
    group = models.CharField(max_length=255, choices=Group.choices, null=True, blank=True)
    subgroup = models.CharField(max_length=255, choices=SubGroup.choices, null=True, blank=True)
    parent_actor = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    payload = models.ForeignKey(Scenario, on_delete=models.CASCADE)

    def __str__(self):
        try:
            string = f"{self.type.lower()[:3]}{self.id} ({self.category})"
        except:
            string = f"actor{self.id} ({self.category})"

        return string


class NonFirmActor(Actor):
    nfATO_capacity_kw = models.FloatField()
    nfATO_starttime = models.FloatField()
    nfATO_endtime = models.FloatField()

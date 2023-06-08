from holon.models import Policy
from src.holon.models.scenario import Scenario
from .repository import RepositoryBaseClass


class PolicyRepository(RepositoryBaseClass):
    """Repository containing all policies in memory"""

    objects: list[Policy] = []

    def __init__(self, scenario: Scenario):
        self.objects = Policy.objects.filter(payload=scenario).get_real_instances()

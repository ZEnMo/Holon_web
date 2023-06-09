from holon.models import GridConnection
from holon.models.scenario import Scenario
from .repository_base import RepositoryBaseClass


class GridConnectionRepository(RepositoryBaseClass):
    """Repository containing all gridconnections in memory"""

    base_model_type = GridConnection

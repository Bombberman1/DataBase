from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SensorDeveloper


class SensorDeveloperDAO(GeneralDAO):
    """
    Realization of SensorDeveloper data access layer.
    """
    _domain_type = SensorDeveloper



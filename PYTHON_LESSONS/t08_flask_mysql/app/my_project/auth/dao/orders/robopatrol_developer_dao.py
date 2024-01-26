from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.robopatrol import RoboPatrol
from my_project.auth.domain.orders.robopatrol_developer import RoboPatrolDeveloper


class RoboPatrolDeveloperDAO(GeneralDAO):
    """
    Realization of RoboPatrolDeveloper data access layer.
    """
    _domain_type = RoboPatrolDeveloper


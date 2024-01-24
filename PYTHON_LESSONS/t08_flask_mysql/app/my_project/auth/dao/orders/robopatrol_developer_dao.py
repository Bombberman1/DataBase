from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.robopatrol import RoboPatrol
from my_project.auth.domain.orders.robopatrol_developer import RoboPatrolDeveloper


class RoboPatrolDeveloperDAO(GeneralDAO):
    """
    Realization of RoboPatrolDeveloper data access layer.
    """
    _domain_type = RoboPatrolDeveloper

    def find_robopatrols(self, robopatrol_developer_id: int) -> List[RoboPatrol]:
        """
        Find RoboPatrols associated with a specific RoboPatrol Developer.
        :param robopatrol_developer_id: ID of the RoboPatrol Developer
        :return: List of RoboPatrol objects associated with the RoboPatrol Developer
        """
        robopatrol_developer = self.find_by_id(robopatrol_developer_id)
        return robopatrol_developer.robopatrols
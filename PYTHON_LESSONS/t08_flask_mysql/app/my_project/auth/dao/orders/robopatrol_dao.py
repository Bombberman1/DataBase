from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.robopatrol import RoboPatrol
from my_project.auth.domain.orders.robopatrol_developer import RoboPatrolDeveloper


class RoboPatrolDAO(GeneralDAO):
    """
    Realization of RoboPatrol data access layer.
    """
    _domain_type = RoboPatrol

    def find_robopatrol_developer(self, robopatrol_id: int) -> RoboPatrolDeveloper:
        """
        Find RoboPatrol Developer associated with a specific RoboPatrol.
        :param robopatrol_id: ID of the RoboPatrol
        :return: RoboPatrolDeveloper object associated with the RoboPatrol
        """
        robopatrol = self.find_by_id(robopatrol_id)
        return robopatrol.robopatrol_developer
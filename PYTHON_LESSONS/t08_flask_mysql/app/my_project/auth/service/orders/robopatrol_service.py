from my_project.auth.dao import robopatrol_dao
from my_project.auth.service.general_service import GeneralService


class RoboPatrolService(GeneralService):
    _dao = robopatrol_dao

    def find_shop(self, robopatrol_id: int):
        return self._dao.find_shop(robopatrol_id)

    def find_purchase(self, robopatrol_id: int):
        return self._dao.find_purchase(robopatrol_id)
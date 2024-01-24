from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import robopatrol_service


class RoboPatrolController(GeneralController):
    _service = robopatrol_service

    def find_shop(self, robopatrol_id: int):
        return self._service.find_shop(robopatrol_id)

    def find_purchase(self, robopatrol_id: int):
        return self._service.find_purchase(robopatrol_id)
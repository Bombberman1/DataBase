from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import robopatrol_service


class RoboPatrolController(GeneralController):
    _service = robopatrol_service

    def find_by_webcam(self, webcam_id: int):
        robopatrols = self._service.find_by_webcam(webcam_id)
        return [robopatrol.put_into_dto() for robopatrol in robopatrols]

    def find_by_sensor(self, sensor_id: int):
        robopatrols = self._service.find_by_sensor(sensor_id)
        return [robopatrol.put_into_dto() for robopatrol in robopatrols]

    def find_by_developer(self, developer_id: int):
        robopatrols = self._service.find_by_developer(developer_id)
        return [robopatrol.put_into_dto() for robopatrol in robopatrols]

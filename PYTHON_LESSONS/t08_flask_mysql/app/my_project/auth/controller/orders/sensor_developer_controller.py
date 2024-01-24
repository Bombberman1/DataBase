from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import sensor_developer_service


class SensorDeveloperController(GeneralController):
    _service = sensor_developer_service

    def find_sensors(self, sensor_developer_id: int):
        return self._service.find_sensors(sensor_developer_id)

    def delete_all_sensors(self, sensor_developer_id: int):
        self._service.delete_all_sensors(sensor_developer_id)
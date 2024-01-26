from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import sensor_service


class SensorController(GeneralController):
    _service = sensor_service

    def find_sensor_developer(self, sensor_id: int):
        return self._service.find_sensor_developer(sensor_id)

    def find_sensors_by_developer_id(self, developer_id: int):
        sensors = self._service.find_sensors_by_developer_id(developer_id)
        return [sensor.put_into_dto() for sensor in sensors]

from my_project.auth.dao import sensor_dao
from my_project.auth.service.general_service import GeneralService


class SensorService(GeneralService):
    _dao = sensor_dao

    def find_sensor_developer(self, sensor_id: int):
        return self._dao.find_sensor_developer(sensor_id)

    def find_sensors_by_developer_id(self, developer_id: int):
        return self._dao.find_sensors_by_developer_id(developer_id)

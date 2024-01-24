from my_project.auth.dao import sensor_developer_dao
from my_project.auth.service.general_service import GeneralService


class SensorDeveloperService(GeneralService):
    _dao = sensor_developer_dao

    def find_sensors(self, sensor_developer_id: int):
        return self._dao.find_sensors(sensor_developer_id)

    def delete_all_sensors(self, sensor_developer_id: int):
        self._dao.delete_all_sensors(sensor_developer_id)


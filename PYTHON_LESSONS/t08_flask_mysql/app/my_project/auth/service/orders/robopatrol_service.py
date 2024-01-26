from my_project.auth.dao import robopatrol_dao
from my_project.auth.service.general_service import GeneralService


class RoboPatrolService(GeneralService):
    _dao = robopatrol_dao

    def find_by_webcam(self, webcam_id: int):
        return self._dao.find_by_webcam(webcam_id)

    def find_by_sensor(self, sensor_id: int):
        return self._dao.find_by_sensor(sensor_id)

    def find_by_developer(self, developer_id: int):
        return self._dao.find_by_developer(developer_id)

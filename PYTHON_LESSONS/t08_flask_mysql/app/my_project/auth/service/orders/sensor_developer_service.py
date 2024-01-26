from my_project.auth.dao import sensor_developer_dao
from my_project.auth.service.general_service import GeneralService


class SensorDeveloperService(GeneralService):
    _dao = sensor_developer_dao

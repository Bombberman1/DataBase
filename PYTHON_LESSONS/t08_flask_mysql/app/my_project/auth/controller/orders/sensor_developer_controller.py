from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import sensor_developer_service


class SensorDeveloperController(GeneralController):
    _service = sensor_developer_service

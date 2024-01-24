from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import robopatrol_developer_service


class RoboPatrolDeveloperController(GeneralController):
    _service = robopatrol_developer_service
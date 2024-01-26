from my_project.auth.dao import robopatrol_developer_dao
from my_project.auth.service.general_service import GeneralService


class RoboPatrolDeveloperService(GeneralService):
    _dao = robopatrol_developer_dao

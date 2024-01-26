from my_project.auth.dao import webcam_developer_dao
from my_project.auth.service.general_service import GeneralService


class WebcamDeveloperService(GeneralService):
    _dao = webcam_developer_dao

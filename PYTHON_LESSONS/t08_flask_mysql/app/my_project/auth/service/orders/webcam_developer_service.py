from my_project.auth.dao import webcam_developer_dao
from my_project.auth.service.general_service import GeneralService


class WebcamDeveloperService(GeneralService):
    _dao = webcam_developer_dao

    def find_webcams(self, webcam_developer_id: int):
        return self._dao.find_webcams(webcam_developer_id)
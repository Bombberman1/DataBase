from my_project.auth.dao import webcam_dao
from my_project.auth.service.general_service import GeneralService


class WebcamService(GeneralService):
    _dao = webcam_dao

    def find_developer(self, webcam_id: int):
        return self._dao.find_developer(webcam_id)

    def find_cameras_by_developer_id(self, developer_id: int):
        return self._dao.find_cameras_by_developer_id(developer_id)

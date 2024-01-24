from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import webcam_developer_service


class WebcamDeveloperController(GeneralController):
    _service = webcam_developer_service

    def find_webcams(self, webcam_developer_id: int):
        return self._service.find_webcams(webcam_developer_id)
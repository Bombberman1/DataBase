from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import webcam_service


class WebcamController(GeneralController):
    _service = webcam_service

    def find_developer(self, webcam_id: int):
        return self._service.find_developer(webcam_id)
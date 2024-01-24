from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import buyer_service


class BuyerController(GeneralController):
    _service = buyer_service

    def find_purchases(self, buyer_id: int):
        return self._service.find_purchases(buyer_id)
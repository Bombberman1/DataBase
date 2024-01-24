from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import purchase_service


class PurchaseController(GeneralController):
    _service = purchase_service

    def find_buyer(self, purchase_id: int):
        return self._service.find_buyer(purchase_id)

    def find_product(self, purchase_id: int):
        return self._service.find_product(purchase_id)

    def find_shop(self, purchase_id: int):
        return self._service.find_shop(purchase_id)
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import buyer_service


class BuyerController(GeneralController):
    _service = buyer_service

    def find_buyers_by_age(self, target_age: int):
        buyers = self._service.find_buyers_by_age(target_age)
        return [buyer.put_into_dto() for buyer in buyers]

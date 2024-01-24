from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import shop_service


class ShopController(GeneralController):
    _service = shop_service

    def find_products(self, shop_id: int):
        return self._service.find_products(shop_id)
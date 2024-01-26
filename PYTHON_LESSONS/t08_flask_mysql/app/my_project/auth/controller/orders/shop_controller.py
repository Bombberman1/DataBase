from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import shop_service


class ShopController(GeneralController):
    _service = shop_service

    def find_shops_by_product_id(self, product_id: int):
        shops = self._service.find_shops_by_product_id(product_id)
        return [shop.put_into_dto() for shop in shops]

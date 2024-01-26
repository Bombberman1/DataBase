from datetime import datetime

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import purchase_service


class PurchaseController(GeneralController):
    _service = purchase_service

    def find_buyer(self, purchase_id: int):
        return self._service.find_buyer(purchase_id)

    def find_robopatrol(self, purchase_id: int):
        return self._service.find_robopatrol(purchase_id)

    def find_shop(self, purchase_id: int):
        return self._service.find_shop(purchase_id)

    def find_purchases_by_date(self, target_date: datetime):
        purchases = self._service.find_purchases_by_date(target_date)
        return [purchase.put_into_dto() for purchase in purchases]

    def find_purchases_by_buyer_id(self, buyer_id: int):
        purchases = self._service.find_purchases_by_buyer_id(buyer_id)
        return [purchase.put_into_dto() for purchase in purchases]

    def find_purchases_by_shop_id(self, shop_id: int):
        purchases = self._service.find_purchases_by_shop_id(shop_id)
        return [purchase.put_into_dto() for purchase in purchases]

    def find_purchases_by_product_id(self, product_id: int):
        purchases = self._service.find_purchases_by_product_id(product_id)
        return [purchase.put_into_dto() for purchase in purchases]

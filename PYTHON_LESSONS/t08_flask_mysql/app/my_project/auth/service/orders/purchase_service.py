from datetime import datetime

from my_project.auth.dao import purchase_dao
from my_project.auth.service.general_service import GeneralService


class PurchaseService(GeneralService):
    _dao = purchase_dao

    def find_buyer(self, purchase_id: int):
        return self._dao.find_buyer(purchase_id)

    def find_robopatrol(self, purchase_id: int):
        return self._dao.find_robopatrol(purchase_id)

    def find_shop(self, purchase_id: int):
        return self._dao.find_shop(purchase_id)

    def find_purchases_by_date(self, target_date: datetime):
        return self._dao.find_purchases_by_date(target_date)

    def find_purchases_by_buyer_id(self, buyer_id: int):
        return self._dao.find_purchases_by_buyer_id(buyer_id)

    def find_purchases_by_shop_id(self, shop_id: int):
        return self._dao.find_purchases_by_shop_id(shop_id)

    def find_purchases_by_product_id(self, product_id: int):
        return self._dao.find_purchases_by_product_id(product_id)

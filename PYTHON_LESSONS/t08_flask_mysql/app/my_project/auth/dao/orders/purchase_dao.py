from datetime import datetime

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.buyer import Buyer
from my_project.auth.domain.orders.purchase import Purchase
from my_project.auth.domain.orders.robopatrol import RoboPatrol
from my_project.auth.domain.orders.shop import Shop


class PurchaseDAO(GeneralDAO):
    """
    Realization of Purchase data access layer.
    """
    _domain_type = Purchase

    def find_buyer(self, purchase_id: int) -> Buyer:
        """
        Find Buyer associated with a specific Purchase.
        :param purchase_id: ID of the Purchase
        :return: Buyer object associated with the Purchase
        """
        purchase = self.find_by_id(purchase_id)
        return purchase.buyer_rel.put_into_dto() if purchase else []

    def find_robopatrol(self, purchase_id: int) -> RoboPatrol:
        """
        Find RoboPatrol associated with a specific Purchase.
        :param purchase_id: ID of the Purchase
        :return: RoboPatrol object associated with the Purchase
        """
        purchase = self.find_by_id(purchase_id)
        return purchase.robopatrol_rel.put_into_dto() if purchase else []

    def find_shop(self, purchase_id: int) -> Shop:
        """
        Find Shop associated with a specific Purchase.
        :param purchase_id: ID of the Purchase
        :return: Shop object associated with the Purchase
        """
        purchase = self.find_by_id(purchase_id)
        return purchase.shop_rel.put_into_dto() if purchase else []

    def find_purchases_by_date(self, target_date: datetime) -> list[Purchase]:
        """
        Find purchases made on a specific date.
        :param target_date: Target date to filter purchases
        :return: List of Purchase objects made on the specified date
        """
        return self._session.query(Purchase).filter(Purchase.deliveryDate == target_date).all()

    def find_purchases_by_buyer_id(self, buyer_id: int) -> list[Purchase]:
        """
        Find purchases made by a specific buyer.
        :param buyer_id: ID of the buyer
        :return: List of Purchase objects made by the specified buyer
        """
        return self._session.query(Purchase).filter(Purchase.buyerId == buyer_id).all()

    def find_purchases_by_shop_id(self, shop_id: int) -> list[Purchase]:
        """
        Find purchases made in a specific shop.
        :param shop_id: ID of the shop
        :return: List of Purchase objects made in the specified shop
        """
        return self._session.query(Purchase).filter(Purchase.shopId == shop_id).all()

    def find_purchases_by_product_id(self, product_id: int) -> list[Purchase]:
        """
        Find purchases made for a specific product.
        :param product_id: ID of the product
        :return: List of Purchase objects made for the specified product
        """
        return self._session.query(Purchase).filter(Purchase.productId == product_id).all()

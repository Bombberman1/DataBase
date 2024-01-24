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
        return purchase.buyer

    def find_robopatrol(self, purchase_id: int) -> RoboPatrol:
        """
        Find RoboPatrol associated with a specific Purchase.
        :param purchase_id: ID of the Purchase
        :return: RoboPatrol object associated with the Purchase
        """
        purchase = self.find_by_id(purchase_id)
        return purchase.robopatrol

    def find_shop(self, purchase_id: int) -> Shop:
        """
        Find Shop associated with a specific Purchase.
        :param purchase_id: ID of the Purchase
        :return: Shop object associated with the Purchase
        """
        purchase = self.find_by_id(purchase_id)
        return purchase.shop
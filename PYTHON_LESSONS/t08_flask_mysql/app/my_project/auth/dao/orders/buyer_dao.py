from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.buyer import Buyer


class BuyerDAO(GeneralDAO):
    """
    Realization of Buyer data access layer.
    """
    _domain_type = Buyer
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.shop import Shop


class ShopDAO(GeneralDAO):
    """
    Realization of Shop data access layer.
    """
    _domain_type = Shop
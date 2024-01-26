from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.shop import Shop


class ShopDAO(GeneralDAO):
    """
    Realization of Shop data access layer.
    """
    _domain_type = Shop

    def find_shops_by_product_id(self, product_id: int) -> list[Shop]:
        """
        Find shops that have a specific product.
        :param product_id: ID of the product
        :return: List of Shop objects where the specified product is available
        """
        return self._session.query(Shop).filter(Shop.productId == product_id).all()

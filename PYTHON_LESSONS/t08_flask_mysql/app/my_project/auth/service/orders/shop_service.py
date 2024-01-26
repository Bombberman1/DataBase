from my_project.auth.dao import shop_dao
from my_project.auth.service.general_service import GeneralService


class ShopService(GeneralService):
    _dao = shop_dao

    def find_shops_by_product_id(self, product_id: int):
        return self._dao.find_shops_by_product_id(product_id)

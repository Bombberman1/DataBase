from my_project.auth.dao import shop_dao
from my_project.auth.service.general_service import GeneralService


class ShopService(GeneralService):
    _dao = shop_dao

    def find_products(self, shop_id: int):
        return self._dao.find_products(shop_id)
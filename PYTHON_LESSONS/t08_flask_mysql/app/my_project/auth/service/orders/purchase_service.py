from my_project.auth.dao import purchase_dao
from my_project.auth.service.general_service import GeneralService


class PurchaseService(GeneralService):
    _dao = purchase_dao

    def find_buyer(self, purchase_id: int):
        return self._dao.find_buyer(purchase_id)

    def find_product(self, purchase_id: int):
        return self._dao.find_product(purchase_id)

    def find_shop(self, purchase_id: int):
        return self._dao.find_shop(purchase_id)
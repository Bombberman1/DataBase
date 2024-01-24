from my_project.auth.dao import buyer_dao
from my_project.auth.service.general_service import GeneralService


class BuyerService(GeneralService):
    _dao = buyer_dao

    def find_purchases(self, buyer_id: int):
        return self._dao.find_purchases(buyer_id)
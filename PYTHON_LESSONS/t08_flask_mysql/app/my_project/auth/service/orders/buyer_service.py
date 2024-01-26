from my_project.auth.dao import buyer_dao
from my_project.auth.service.general_service import GeneralService


class BuyerService(GeneralService):
    _dao = buyer_dao

    def find_buyers_by_age(self, target_age: int):
        return self._dao.find_buyers_by_age(target_age)

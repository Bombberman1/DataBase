from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.buyer import Buyer


class BuyerDAO(GeneralDAO):
    """
    Realization of Buyer data access layer.
    """
    _domain_type = Buyer

    def find_buyers_by_age(self, target_age: int) -> list[Buyer]:
        """
        Find buyers with a specific age.
        :param target_age: Target age to filter buyers
        :return: List of Buyer objects with the specified age
        """
        return self._session.query(Buyer).filter(Buyer.age == target_age).all()

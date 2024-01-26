from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Child(db.Model, IDto):
    """
    Model declaration for Child table.
    """
    __tablename__ = "child"

    childId = db.Column(db.Integer, primary_key=True)
    buyerId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    school = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Child({self.childId}, {self.buyerId}, '{self.name}', {self.age}, '{self.school}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "childId": self.childId,
            "buyerId": self.buyerId,
            "name": self.name,
            "age": self.age,
            "school": self.school,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Child':
        obj = Child(
            buyerId=dto_dict.get("buyerId"),
            name=dto_dict.get("name"),
            age=dto_dict.get("age"),
            school=dto_dict.get("school"),
        )
        return obj

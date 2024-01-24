from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Buyer(db.Model, IDto):
    """
    Model declaration for Buyer table.
    """
    __tablename__ = "buyer"

    userId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)

    purchases = db.relationship('Purchase', back_populates='buyer_rel', lazy=True)

    def __repr__(self) -> str:
        return f"Buyer({self.userId}, '{self.name}', {self.age}, '{self.gender}', '{self.location}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "userId": self.userId,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "location": self.location,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Buyer':
        obj = Buyer(
            name=dto_dict.get("name"),
            age=dto_dict.get("age"),
            gender=dto_dict.get("gender"),
            location=dto_dict.get("location"),
        )
        return obj

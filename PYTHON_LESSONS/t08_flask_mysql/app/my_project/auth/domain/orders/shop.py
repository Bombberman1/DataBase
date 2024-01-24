from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Shop(db.Model, IDto):
    __tablename__ = "shop"

    shopId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('robopatrol.robopatrolId'), nullable=False)

    robopatrols = db.relationship('RoboPatrol', back_populates='shop')
    purchases = db.relationship('Purchase', back_populates='shop_rel')

    def __repr__(self) -> str:
        return f"Shop({self.shopId}, '{self.name}', '{self.location}', {self.productId})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "shopId": self.shopId,
            "name": self.name,
            "location": self.location,
            "productId": self.productId,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Shop':
        obj = Shop(
            name=dto_dict.get("name"),
            location=dto_dict.get("location"),
            productId=dto_dict.get("productId"),
        )
        return obj

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Purchase(db.Model, IDto):
    __tablename__ = "purchase"

    purchaseId = db.Column(db.Integer, primary_key=True)
    buyerId = db.Column(db.Integer, db.ForeignKey('buyer.userId'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('robopatrol.robopatrolId'), nullable=False)
    shopId = db.Column(db.Integer, db.ForeignKey('shop.shopId'), nullable=False)
    deliveryDate = db.Column(db.DATE, nullable=False)

    buyer_rel = db.relationship('Buyer', back_populates='purchases')
    robopatrol_rel = db.relationship('RoboPatrol', back_populates='purchases')
    shop_rel = db.relationship('Shop', back_populates='purchases')

    def __repr__(self) -> str:
        return f"Purchase({self.purchaseId}, {self.buyerId}, {self.productId}, {self.shopId}, '{self.deliveryDate}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "purchaseId": self.purchaseId,
            "buyerId": self.buyerId,
            "productId": self.productId,
            "shopId": self.shopId,
            "deliveryDate": str(self.deliveryDate),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Purchase':
        obj = Purchase(
            buyerId=dto_dict.get("buyerId"),
            productId=dto_dict.get("productId"),
            shopId=dto_dict.get("shopId"),
            deliveryDate=dto_dict.get("deliveryDate"),
        )
        return obj

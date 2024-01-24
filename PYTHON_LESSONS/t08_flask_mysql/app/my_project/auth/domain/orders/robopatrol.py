from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RoboPatrol(db.Model, IDto):
    __tablename__ = "robopatrol"

    robopatrolId = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45), nullable=False)
    price = db.Column(db.DECIMAL(12, 2), nullable=False)
    developerId = db.Column(db.Integer, db.ForeignKey('robopatrolDeveloper.robopatrolDeveloperId'), nullable=False)
    sensorId = db.Column(db.Integer, db.ForeignKey('sensor.sensorId'), nullable=False)
    webcamId = db.Column(db.Integer, db.ForeignKey('webcam.webcamId'), nullable=False)

    developer_rel = db.relationship('RoboPatrolDeveloper', back_populates='robopatrols')
    sensor_rel = db.relationship('Sensor', back_populates='robopatrols')
    webcam_rel = db.relationship('Webcam', back_populates='robopatrols')
    purchases = db.relationship('Purchase', back_populates='robopatrol_rel')
    shop = db.relationship('Shop', back_populates='robopatrols')

    def __repr__(self) -> str:
        return f"Robopatrol({self.robopatrolId}, '{self.model}', {self.price}, {self.developerId}, {self.sensorId}, {self.webcamId})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "robopatrolId": self.robopatrolId,
            "model": self.model,
            "price": float(self.price),
            "developerId": self.developerId,
            "sensorId": self.sensorId,
            "webcamId": self.webcamId,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'RoboPatrol':
        obj = RoboPatrol(
            model=dto_dict.get("model"),
            price=dto_dict.get("price"),
            developerId=dto_dict.get("developerId"),
            sensorId=dto_dict.get("sensorId"),
            webcamId=dto_dict.get("webcamId"),
        )
        return obj

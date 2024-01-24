from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Sensor(db.Model, IDto):
    __tablename__ = "sensor"

    sensorId = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(45), nullable=False)
    model = db.Column(db.String(45), nullable=False)
    developerId = db.Column(db.Integer, db.ForeignKey('sensorDeveloper.sensorDeveloperId'), nullable=False)

    developer_rel = db.relationship('SensorDeveloper', back_populates='sensors')
    robopatrols = db.relationship('RoboPatrol', back_populates='sensor_rel')

    def __repr__(self) -> str:
        return f"Sensor({self.sensorId}, '{self.type}', '{self.model}', {self.developerId})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sensorId": self.sensorId,
            "type": self.type,
            "model": self.model,
            "developerId": self.developerId,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Sensor':
        obj = Sensor(
            type=dto_dict.get("type"),
            model=dto_dict.get("model"),
            developerId=dto_dict.get("developerId"),
        )
        return obj

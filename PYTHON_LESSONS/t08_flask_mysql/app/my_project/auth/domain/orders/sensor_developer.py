from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class SensorDeveloper(db.Model, IDto):
    __tablename__ = "sensorDeveloper"

    sensorDeveloperId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    sensors = db.relationship('Sensor', back_populates='developer_rel', lazy=True)

    def __repr__(self) -> str:
        return f"SensorDeveloper({self.sensorDeveloperId}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sensorDeveloperId": self.sensorDeveloperId,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'SensorDeveloper':
        obj = SensorDeveloper(
            name=dto_dict.get("name"),
        )
        return obj

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RoboPatrolDeveloper(db.Model, IDto):
    __tablename__ = "robopatrolDeveloper"

    robopatrolDeveloperId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    robopatrols = db.relationship('RoboPatrol', back_populates='developer_rel')

    def __repr__(self) -> str:
        return f"RobopatrolDeveloper({self.robopatrolDeveloperId}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "robopatrolDeveloperId": self.robopatrolDeveloperId,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'RoboPatrolDeveloper':
        obj = RoboPatrolDeveloper(
            name=dto_dict.get("name"),
        )
        return obj

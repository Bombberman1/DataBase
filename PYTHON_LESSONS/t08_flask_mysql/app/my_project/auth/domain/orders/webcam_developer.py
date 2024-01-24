from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class WebCamDeveloper(db.Model, IDto):
    __tablename__ = "webcamDeveloper"

    webcamDeveloperId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    webcams = db.relationship('Webcam', back_populates='developer_rel', lazy=True)

    def __repr__(self) -> str:
        return f"WebcamDeveloper({self.webcamDeveloperId}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "webcamDeveloperId": self.webcamDeveloperId,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'WebCamDeveloper':
        obj = WebCamDeveloper(
            name=dto_dict.get("name"),
        )
        return obj

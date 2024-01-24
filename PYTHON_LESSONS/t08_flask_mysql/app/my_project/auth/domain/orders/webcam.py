from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Webcam(db.Model, IDto):
    __tablename__ = "webcam"

    webcamId = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45), nullable=False)
    megapixels = db.Column(db.Integer, nullable=False)
    recordingFps = db.Column(db.Integer, nullable=False)
    recordingQuality = db.Column(db.String(45), nullable=False)
    developerId = db.Column(db.Integer, db.ForeignKey('webcamDeveloper.webcamDeveloperId'), nullable=False)

    developer_rel = db.relationship('WebCamDeveloper', back_populates='webcams')
    robopatrols = db.relationship('RoboPatrol', back_populates='webcam_rel')

    def __repr__(self) -> str:
        return f"Webcam({self.webcamId}, '{self.model}', {self.megapixels}, {self.recordingFps}, '{self.recordingQuality}', {self.developerId})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "webcamId": self.webcamId,
            "model": self.model,
            "megapixels": self.megapixels,
            "recordingFps": self.recordingFps,
            "recordingQuality": self.recordingQuality,
            "developerId": self.developerId,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Webcam':
        obj = Webcam(
            model=dto_dict.get("model"),
            megapixels=dto_dict.get("megapixels"),
            recordingFps=dto_dict.get("recordingFps"),
            recordingQuality=dto_dict.get("recordingQuality"),
            developerId=dto_dict.get("developerId"),
        )
        return obj

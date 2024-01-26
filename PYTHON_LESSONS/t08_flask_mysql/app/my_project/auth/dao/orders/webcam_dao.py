from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.webcam import Webcam
from my_project.auth.domain.orders.webcam_developer import WebCamDeveloper


class WebcamDAO(GeneralDAO):
    """
    Realization of WebCam data access layer.
    """
    _domain_type = Webcam

    def find_developer(self, webcam_id: int) -> object:
        """
        Find the WebCam Developer associated with a specific WebCam.
        :param webcam_id: ID of the WebCam
        :return: WebCam Developer object associated with the WebCam
        """

        webcam = self._session.query(Webcam).options(joinedload(Webcam.developer_rel)).get(webcam_id)

        return webcam.developer_rel.put_into_dto() if webcam and webcam.developer_rel else []

    def find_cameras_by_developer_id(self, developer_id: int) -> list[Webcam]:
        """
        Find cameras developed by a specific webcam developer.
        :param developer_id: ID of the webcam developer
        :return: List of Webcam objects developed by the specified webcam developer
        """
        return self._session.query(Webcam).join(Webcam.developer_rel).filter(
            WebCamDeveloper.webcamDeveloperId == developer_id).all()

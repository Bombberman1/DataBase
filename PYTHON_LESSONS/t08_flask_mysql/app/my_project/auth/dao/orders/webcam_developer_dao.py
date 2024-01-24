from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.webcam import Webcam
from my_project.auth.domain.orders.webcam_developer import WebCamDeveloper


class WebcamDeveloperDAO(GeneralDAO):
    """
    Realization of WebcamDeveloper data access layer.
    """
    _domain_type = WebCamDeveloper

    def find_webcams(self, webcam_developer_id: int) -> List[object]:
        """
        Find webcams associated with a specific Webcam Developer.
        :param webcam_developer_id: ID of the Webcam Developer
        :return: List of Webcam objects associated with the Webcam Developer
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the Webcam table to get the Webcam objects associated with the Webcam Developer
        webcams = session.query(Webcam).filter(Webcam.developerId == webcam_developer_id).all()

        return [webcam.put_into_dto() for webcam in webcams]
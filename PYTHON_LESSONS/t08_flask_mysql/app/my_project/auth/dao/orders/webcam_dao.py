from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.webcam import Webcam


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
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the WebCam table to get the WebCam object
        webcam = session.query(Webcam).options(joinedload(Webcam.developer)).get(webcam_id)

        return webcam.developer.put_into_dto() if webcam and webcam.developer else None

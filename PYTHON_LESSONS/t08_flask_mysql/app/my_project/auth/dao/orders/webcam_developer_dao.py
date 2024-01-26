from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.webcam_developer import WebCamDeveloper


class WebcamDeveloperDAO(GeneralDAO):
    """
    Realization of WebcamDeveloper data access layer.
    """
    _domain_type = WebCamDeveloper


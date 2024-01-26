from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.robopatrol import RoboPatrol
from my_project.auth.domain.orders.robopatrol_developer import RoboPatrolDeveloper
from my_project.auth.domain.orders.sensor import Sensor
from my_project.auth.domain.orders.webcam import Webcam


class RoboPatrolDAO(GeneralDAO):
    """
    Realization of RoboPatrol data access layer.
    """
    _domain_type = RoboPatrol

    def find_by_webcam(self, webcam_id: int) -> list[RoboPatrol]:
        """
        Find all RoboPatrols that have a specific webcam.
        :param webcam_id: ID of the webcam
        :return: List of RoboPatrol objects with the specified webcam
        """
        return self._session.query(RoboPatrol).join(RoboPatrol.webcam_rel).filter(Webcam.webcamId == webcam_id).all()

    def find_by_sensor(self, sensor_id: int) -> list[RoboPatrol]:
        """
        Find all RoboPatrols that have a specific sensor.
        :param sensor_id: ID of the sensor
        :return: List of RoboPatrol objects with the specified sensor
        """
        return self._session.query(RoboPatrol).join(RoboPatrol.sensor_rel).filter(Sensor.sensorId == sensor_id).all()

    def find_by_developer(self, developer_id: int) -> list[RoboPatrol]:
        """
        Find all RoboPatrols that have a specific developer.
        :param developer_id: ID of the developer
        :return: List of RoboPatrol objects with the specified developer
        """
        return self._session.query(RoboPatrol).join(RoboPatrol.developer_rel).filter(RoboPatrolDeveloper.robopatrolDeveloperId == developer_id).all()

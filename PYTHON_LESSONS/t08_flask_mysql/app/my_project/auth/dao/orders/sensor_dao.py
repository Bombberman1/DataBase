from typing import List

from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Sensor

from my_project.auth.domain.orders.sensor_developer import SensorDeveloper


class SensorDAO(GeneralDAO):
    """
    Realization of Sensor data access layer.
    """
    _domain_type = Sensor

    def find_sensor_developer(self, sensor_id: int) -> object:
        """
        Find the Sensor Developer associated with a specific Sensor.
        :param sensor_id: ID of the Sensor
        :return: Sensor Developer object associated with the Sensor
        """

        sensor = self._session.query(Sensor).options(joinedload(Sensor.developer_rel)).get(sensor_id)

        return sensor.developer_rel.put_into_dto() if sensor and sensor.developer_rel else []

    def find_sensors_by_developer_id(self, developer_id: int) -> list[Sensor]:
        """
        Find sensors associated with a specific sensor developer.
        :param developer_id: ID of the sensor developer
        :return: List of Sensor objects associated with the specified sensor developer
        """
        return self._session.query(Sensor).filter(Sensor.developerId == developer_id).all()

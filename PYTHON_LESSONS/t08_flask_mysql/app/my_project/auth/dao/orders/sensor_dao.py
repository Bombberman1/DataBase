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
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the Sensor Developer ID associated with the Sensor
        sensor = session.query(Sensor).options(joinedload(Sensor.developer_rel)).get(sensor_id)

        return sensor.developer_rel.put_into_dto() if sensor and sensor.developer_rel else None


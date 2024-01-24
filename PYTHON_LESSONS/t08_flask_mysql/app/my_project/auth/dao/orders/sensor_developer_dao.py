from abc import ABC
from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Mapper, joinedload

from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SensorDeveloper

from my_project.auth.domain.orders.sensor import Sensor


class SensorDeveloperDAO(GeneralDAO):
    """
    Realization of SensorDeveloper data access layer.
    """
    _domain_type = SensorDeveloper

    def find_sensors(self, developer_id: int):
        """
        Find all Sensors associated with a specific Sensor Developer.
        :param developer_id: ID of the Sensor Developer
        :return: List of Sensor objects associated with the Sensor Developer
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the Sensor table to get all Sensor objects associated with the given Sensor Developer ID
        sensors = session.query(Sensor).options(joinedload(Sensor.developer_rel)).filter(Sensor.developer_rel.sensorDeveloperId == developer_id).all()

        return [sensor.put_into_dto() for sensor in sensors] if sensors else []

    def delete_all_sensors(self, developer_id: int):
        """
        Delete all Sensors associated with a specific Sensor Developer.
        :param developer_id: ID of the Sensor Developer
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Delete all Sensors associated with the given Sensor Developer ID
        session.query(Sensor).filter(Sensor.developer_rel.sensorDeveloperId == developer_id).delete()

        # Commit the changes to the database
        session.commit()

from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import sensor_developer_controller
from my_project.auth.domain.orders.sensor_developer import SensorDeveloper

sensor_dev_bp = Blueprint('sensor_developers', __name__, url_prefix='/sensor-developers')


@sensor_dev_bp.get('')
def get_all_sensor_developers() -> Response:
    return make_response(jsonify(sensor_developer_controller.find_all()), HTTPStatus.OK)


@sensor_dev_bp.post('')
def create_sensor_developer() -> Response:
    content = request.get_json()
    sensor_dev = SensorDeveloper.create_from_dto(content)
    sensor_developer_controller.create(sensor_dev)
    return make_response(jsonify(sensor_dev.put_into_dto()), HTTPStatus.CREATED)


@sensor_dev_bp.get('/<int:sensor_dev_id>')
def get_sensor_developer(sensor_dev_id: int) -> Response:
    return make_response(jsonify(sensor_developer_controller.find_by_id(sensor_dev_id)), HTTPStatus.OK)


@sensor_dev_bp.put('/<int:sensor_dev_id>')
def update_sensor_developer(sensor_dev_id: int) -> Response:
    content = request.get_json()
    sensor_dev = SensorDeveloper.create_from_dto(content)
    sensor_developer_controller.update(sensor_dev_id, sensor_dev)
    return make_response("Sensor developer updated", HTTPStatus.OK)


@sensor_dev_bp.patch('/<int:sensor_dev_id>')
def patch_sensor_developer(sensor_dev_id: int) -> Response:
    content = request.get_json()
    sensor_developer_controller.patch(sensor_dev_id, content)
    return make_response("Sensor developer updated", HTTPStatus.OK)


@sensor_dev_bp.delete('/<int:sensor_dev_id>')
def delete_sensor_developer(sensor_dev_id: int) -> Response:
    sensor_developer_controller.delete(sensor_dev_id)
    return make_response("Sensor developer deleted", HTTPStatus.OK)

from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import robopatrol_controller
from my_project.auth.domain.orders.robopatrol import RoboPatrol

robo_patrol_bp = Blueprint('robo_patrols', __name__, url_prefix='/robo_patrols')


@robo_patrol_bp.get('')
def get_all_robo_patrols() -> Response:
    return make_response(jsonify(robopatrol_controller.find_all()), HTTPStatus.OK)


@robo_patrol_bp.get('/<int:robo_patrol_id>/robo_patrol_developer')
def get_robo_patrol_developer(robo_patrol_id: int) -> Response:
    return make_response(jsonify(robopatrol_controller.find_robo_patrol_developer(robo_patrol_id)), HTTPStatus.OK)


@robo_patrol_bp.post('')
def create_robo_patrol() -> Response:
    content = request.get_json()
    robo_patrol = RoboPatrol.create_from_dto(content)
    robopatrol_controller.create(robo_patrol)
    return make_response(jsonify(robo_patrol.put_into_dto()), HTTPStatus.CREATED)


@robo_patrol_bp.get('/<int:robo_patrol_id>')
def get_robo_patrol(robo_patrol_id: int) -> Response:
    return make_response(jsonify(robopatrol_controller.find_by_id(robo_patrol_id)), HTTPStatus.OK)


@robo_patrol_bp.put('/<int:robo_patrol_id>')
def update_robo_patrol(robo_patrol_id: int) -> Response:
    content = request.get_json()
    robo_patrol = RoboPatrol.create_from_dto(content)
    robopatrol_controller.update(robo_patrol_id, robo_patrol)
    return make_response("Robo patrol updated", HTTPStatus.OK)


@robo_patrol_bp.patch('/<int:robo_patrol_id>')
def patch_robo_patrol(robo_patrol_id: int) -> Response:
    content = request.get_json()
    robopatrol_controller.patch(robo_patrol_id, content)
    return make_response("Robo patrol updated", HTTPStatus.OK)


@robo_patrol_bp.delete('/<int:robo_patrol_id>')
def delete_robo_patrol(robo_patrol_id: int) -> Response:
    robopatrol_controller.delete(robo_patrol_id)
    return make_response("Robo patrol deleted", HTTPStatus.OK)


@robo_patrol_bp.get('/webcam/<int:webcam_id>')
def get_robo_patrols_by_webcam(webcam_id: int) -> Response:
    return make_response(jsonify(robopatrol_controller.find_by_webcam(webcam_id)), HTTPStatus.OK)


@robo_patrol_bp.get('/sensor/<int:sensor_id>')
def get_robo_patrols_by_sensor(sensor_id: int) -> Response:
    return make_response(jsonify(robopatrol_controller.find_by_sensor(sensor_id)), HTTPStatus.OK)


@robo_patrol_bp.get('/developer/<int:developer_id>')
def get_robo_patrols_by_developer(developer_id: int) -> Response:
    return make_response(jsonify(robopatrol_controller.find_by_developer(developer_id)), HTTPStatus.OK)

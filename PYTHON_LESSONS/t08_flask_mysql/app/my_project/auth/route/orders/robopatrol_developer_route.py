from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import robopatrol_developer_controller
from my_project.auth.domain.orders.robopatrol_developer import RoboPatrolDeveloper

robo_patrol_developer_bp = Blueprint('robo_patrol_developers', __name__, url_prefix='/robo_patrol_developers')


@robo_patrol_developer_bp.get('')
def get_all_robo_patrol_developers() -> Response:
    return make_response(jsonify(robopatrol_developer_controller.find_all()), HTTPStatus.OK)


@robo_patrol_developer_bp.get('/<int:robo_patrol_developer_id>/robo_patrols')
def get_all_robo_patrols(robo_patrol_developer_id: int) -> Response:
    return make_response(jsonify(robopatrol_developer_controller.find_robo_patrols(robo_patrol_developer_id)), HTTPStatus.OK)


@robo_patrol_developer_bp.delete('/<int:robo_patrol_developer_id>/robo_patrols')
def delete_all_robo_patrols(robo_patrol_developer_id: int) -> Response:
    robopatrol_developer_controller.delete_all_robo_patrols(robo_patrol_developer_id)
    return make_response("Robo patrols deleted", HTTPStatus.OK)


@robo_patrol_developer_bp.post('')
def create_robo_patrol_developer() -> Response:
    content = request.get_json()
    robo_patrol_developer = RoboPatrolDeveloper.create_from_dto(content)
    robopatrol_developer_controller.create(robo_patrol_developer)
    return make_response(jsonify(robo_patrol_developer.put_into_dto()), HTTPStatus.CREATED)


@robo_patrol_developer_bp.get('/<int:robo_patrol_developer_id>')
def get_robo_patrol_developer(robo_patrol_developer_id: int) -> Response:
    return make_response(jsonify(robopatrol_developer_controller.find_by_id(robo_patrol_developer_id)), HTTPStatus.OK)


@robo_patrol_developer_bp.put('/<int:robo_patrol_developer_id>')
def update_robo_patrol_developer(robo_patrol_developer_id: int) -> Response:
    content = request.get_json()
    robo_patrol_developer = RoboPatrolDeveloper.create_from_dto(content)
    robopatrol_developer_controller.update(robo_patrol_developer_id, robo_patrol_developer)
    return make_response("Robo patrol developer updated", HTTPStatus.OK)


@robo_patrol_developer_bp.patch('/<int:robo_patrol_developer_id>')
def patch_robo_patrol_developer(robo_patrol_developer_id: int) -> Response:
    content = request.get_json()
    robopatrol_developer_controller.patch(robo_patrol_developer_id, content)
    return make_response("Robo patrol developer updated", HTTPStatus.OK)


@robo_patrol_developer_bp.delete('/<int:robo_patrol_developer_id>')
def delete_robo_patrol_developer(robo_patrol_developer_id: int) -> Response:
    robopatrol_developer_controller.delete(robo_patrol_developer_id)
    return make_response("Robo patrol developer deleted", HTTPStatus.OK)

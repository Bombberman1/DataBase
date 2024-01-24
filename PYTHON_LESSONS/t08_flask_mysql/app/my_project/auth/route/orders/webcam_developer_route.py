from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import webcam_developer_controller
from my_project.auth.domain.orders.webcam_developer import WebCamDeveloper

webcam_dev_bp = Blueprint('webcam_developers', __name__, url_prefix='/webcam-developers')


@webcam_dev_bp.get('')
def get_all_webcam_developers() -> Response:
    return make_response(jsonify(webcam_developer_controller.find_all()), HTTPStatus.OK)


@webcam_dev_bp.post('')
def create_webcam_developer() -> Response:
    content = request.get_json()
    webcam_dev = WebCamDeveloper.create_from_dto(content)
    webcam_developer_controller.create(webcam_dev)
    return make_response(jsonify(webcam_dev.put_into_dto()), HTTPStatus.CREATED)


@webcam_dev_bp.get('/<int:webcam_dev_id>')
def get_webcam_developer(webcam_dev_id: int) -> Response:
    return make_response(jsonify(webcam_developer_controller.find_by_id(webcam_dev_id)), HTTPStatus.OK)


@webcam_dev_bp.put('/<int:webcam_dev_id>')
def update_webcam_developer(webcam_dev_id: int) -> Response:
    content = request.get_json()
    webcam_dev = WebCamDeveloper.create_from_dto(content)
    webcam_developer_controller.update(webcam_dev_id, webcam_dev)
    return make_response("Webcam Developer updated", HTTPStatus.OK)


@webcam_dev_bp.patch('/<int:webcam_dev_id>')
def patch_webcam_developer(webcam_dev_id: int) -> Response:
    content = request.get_json()
    webcam_developer_controller.patch(webcam_dev_id, content)
    return make_response("Webcam Developer updated", HTTPStatus.OK)


@webcam_dev_bp.delete('/<int:webcam_dev_id>')
def delete_webcam_developer(webcam_dev_id: int) -> Response:
    webcam_developer_controller.delete(webcam_dev_id)
    return make_response("Webcam Developer deleted", HTTPStatus.OK)

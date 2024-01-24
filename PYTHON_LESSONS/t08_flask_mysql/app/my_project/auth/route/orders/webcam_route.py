from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import webcam_controller
from my_project.auth.dao.orders.webcam_dao import Webcam

webcam_bp = Blueprint('webcams', __name__, url_prefix='/webcams')


@webcam_bp.get('')
def get_all_webcams() -> Response:
    return make_response(jsonify(webcam_controller.find_all()), HTTPStatus.OK)


@webcam_bp.post('')
def create_webcam() -> Response:
    content = request.get_json()
    webcam = Webcam.create_from_dto(content)
    webcam_controller.create(webcam)
    return make_response(jsonify(webcam.put_into_dto()), HTTPStatus.CREATED)


@webcam_bp.get('/<int:webcam_id>')
def get_webcam(webcam_id: int) -> Response:
    return make_response(jsonify(webcam_controller.find_by_id(webcam_id)), HTTPStatus.OK)


@webcam_bp.put('/<int:webcam_id>')
def update_webcam(webcam_id: int) -> Response:
    content = request.get_json()
    webcam = Webcam.create_from_dto(content)
    webcam_controller.update(webcam_id, webcam)
    return make_response("Webcam updated", HTTPStatus.OK)


@webcam_bp.patch('/<int:webcam_id>')
def patch_webcam(webcam_id: int) -> Response:
    content = request.get_json()
    webcam_controller.patch(webcam_id, content)
    return make_response("Webcam updated", HTTPStatus.OK)


@webcam_bp.delete('/<int:webcam_id>')
def delete_webcam(webcam_id: int) -> Response:
    webcam_controller.delete(webcam_id)
    return make_response("Webcam deleted", HTTPStatus.OK)


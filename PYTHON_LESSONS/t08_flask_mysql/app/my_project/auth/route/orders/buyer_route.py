from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import buyer_controller
from my_project.auth.domain.orders.buyer import Buyer

buyer_bp = Blueprint('buyers', __name__, url_prefix='/buyers')


@buyer_bp.get('')
def get_all_buyers() -> Response:
    return make_response(jsonify(buyer_controller.find_all()), HTTPStatus.OK)


@buyer_bp.post('')
def create_buyer() -> Response:
    content = request.get_json()
    buyer = Buyer.create_from_dto(content)
    buyer_controller.create(buyer)
    return make_response(jsonify(buyer.put_into_dto()), HTTPStatus.CREATED)


@buyer_bp.get('/<int:buyer_id>')
def get_buyer(buyer_id: int) -> Response:
    return make_response(jsonify(buyer_controller.find_by_id(buyer_id)), HTTPStatus.OK)


@buyer_bp.put('/<int:buyer_id>')
def update_buyer(buyer_id: int) -> Response:
    content = request.get_json()
    buyer = Buyer.create_from_dto(content)
    buyer_controller.update(buyer_id, buyer)
    return make_response("Buyer updated", HTTPStatus.OK)


@buyer_bp.patch('/<int:buyer_id>')
def patch_buyer(buyer_id: int) -> Response:
    content = request.get_json()
    buyer_controller.patch(buyer_id, content)
    return make_response("Buyer updated", HTTPStatus.OK)


@buyer_bp.delete('/<int:buyer_id>')
def delete_buyer(buyer_id: int) -> Response:
    buyer_controller.delete(buyer_id)
    return make_response("Buyer deleted", HTTPStatus.OK)

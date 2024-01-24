from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from my_project.auth.controller import purchase_controller
from my_project.auth.domain.orders.purchase import Purchase

purchase_bp = Blueprint('purchases', __name__, url_prefix='/purchases')


@purchase_bp.get('')
def get_all_purchases() -> Response:
    return make_response(jsonify(purchase_controller.find_all()), HTTPStatus.OK)


@purchase_bp.post('')
def create_purchase() -> Response:
    content = request.get_json()
    purchase = Purchase.create_from_dto(content)
    purchase_controller.create(purchase)
    return make_response(jsonify(purchase.put_into_dto()), HTTPStatus.CREATED)


@purchase_bp.get('/<int:purchase_id>')
def get_purchase(purchase_id: int) -> Response:
    return make_response(jsonify(purchase_controller.find_by_id(purchase_id)), HTTPStatus.OK)


@purchase_bp.put('/<int:purchase_id>')
def update_purchase(purchase_id: int) -> Response:
    content = request.get_json()
    purchase = Purchase.create_from_dto(content)
    purchase_controller.update(purchase_id, purchase)
    return make_response("Purchase updated", HTTPStatus.OK)


@purchase_bp.patch('/<int:purchase_id>')
def patch_purchase(purchase_id: int) -> Response:
    content = request.get_json()
    purchase_controller.patch(purchase_id, content)
    return make_response("Purchase updated", HTTPStatus.OK)


@purchase_bp.delete('/<int:purchase_id>')
def delete_purchase(purchase_id: int) -> Response:
    purchase_controller.delete(purchase_id)
    return make_response("Purchase deleted", HTTPStatus.OK)

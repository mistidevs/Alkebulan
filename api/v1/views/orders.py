#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Orders """
from models.order import Order
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/orders', methods=['GET'], strict_slashes=False)
def get_orders():
    """
    Retrieves the list of all Order objects
    or a specific Order
    """
    all_orders = storage.all(Order).values()
    list_orders = []
    for order in all_orders:
        list_orders.append(order.to_dict())
    return jsonify(list_orders)


@app_views.route('/orders/<order_id>', methods=['GET'], strict_slashes=False)
def get_order(order_id):
    """ Retrieves a order """
    order = storage.get(Order, order_id)
    if not order:
        abort(404)

    return jsonify(order.to_dict())


@app_views.route('/orders/<order_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/order/delete_order.yml', methods=['DELETE'])
def delete_order(order_id):
    """
    Deletes a order Object
    """

    order = storage.get(Order, order_id)

    if not order:
        abort(404)

    storage.delete(order)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/orders', methods=['POST'], strict_slashes=False)
@swag_from('documentation/order/post_order.yml', methods=['POST'])
def post_order():
    """
    Creates a order
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'product_id' not in request.get_json():
        abort(400, description="Missing product id")
    if 'farmer_id' not in request.get_json():
        abort(400, "Missing farmer id")
    if 'consumer_id' not in request.get_json():
        abort(400, "Missing consumer id")
    if 'order_date' not in request.get_json():
        abort(400, "Missing order date")
    if 'quantity' not in request.get_json():
        abort(400, "Missing quantity")
    if 'unit_price' not in request.get_json():
        abort(400, "Missing unit price")
    if 'total_price' not in request.get_json():
        abort(400, "Missing total price")

    data = request.get_json()
    instance = Order(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
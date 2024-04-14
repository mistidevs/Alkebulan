#!/usr/bin/python3
"""
Methods that handle all default RESTFul API actions for Consumers
"""
from models.consumer import Consumer
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/consumers', methods=['GET'], strict_slashes=False)
def get_consumers():
    """
    Retrieves the list of all Consumer objects
    or a specific Consumer
    """
    all_consumers = storage.all(Consumer).values()
    list_consumers = []
    for consumer in all_consumers:
        list_consumers.append(consumer.to_dict())
    return jsonify(list_consumers)


@app_views.route('/consumers/<consumer_id>', methods=['GET'], strict_slashes=False)
def get_consumer(consumer_id):
    """
    Retrieves a Consumer
    """
    consumer = storage.get(Consumer, consumer_id)
    if not consumer:
        abort(404)

    return jsonify(consumer.to_dict())


@app_views.route('/consumers/<consumer_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_consumer(consumer_id):
    """
    Deletes a Consumer
    """
    consumer = storage.get(Consumer, consumer_id)

    if not consumer:
        abort(404)

    storage.delete(consumer)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/consumers', methods=['POST'], strict_slashes=False)
def post_consumer():
    """
    Creates a Consumer
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    if 'user_name' not in request.get_json():
        abort(400, "Missing user name")
    if 'full_name' not in request.get_json():
        abort(400, "Missing full name")
    if 'phone_number' not in request.get_json():
        
        abort(400, "Missing phone number")

    data = request.get_json()
    instance = Consumer(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/consumers/<consumer_id>', methods=['PUT'], strict_slashes=False)
def put_consumer(consumer_id):
    """
    Updates a Consumer
    """
    consumer = storage.get(Consumer, consumer_id)

    if not consumer:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(consumer, key, value)
    storage.save()
    return make_response(jsonify(consumer.to_dict()), 200)
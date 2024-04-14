#!/usr/bin/python3
"""
Methods that handle all default RESTFul API actions for Farmers
"""
from models.farmer import Farmer
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/farmers', methods=['GET'], strict_slashes=False)
def get_farmers():
    """
    Retrieves the list of all Farmer objects
    or a specific Farmer
    """
    all_farmers = storage.all(Farmer).values()
    list_farmers = []
    for farmer in all_farmers:
        list_farmers.append(farmer.to_dict())
    return jsonify(list_farmers)


@app_views.route('/farmers/<farmer_id>', methods=['GET'], strict_slashes=False)
def get_farmer(farmer_id):
    """
    Retrieves a Farmer
    """
    farmer = storage.get(Farmer, farmer_id)
    if not farmer:
        abort(404)

    return jsonify(farmer.to_dict())


@app_views.route('/farmers/<farmer_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_farmer(farmer_id):
    """
    Deletes a Farmer
    """
    farmer = storage.get(Farmer, farmer_id)

    if not farmer:
        abort(404)

    storage.delete(farmer)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/farmers', methods=['POST'], strict_slashes=False)
def post_farmer():
    """
    Creates a farmer
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
    if 'location' not in request.get_json():
        abort(400, "Missing location")
    if 'latitude' not in request.get_json():
        abort(400, "Missing latitude")
    if 'longitude' not in request.get_json():
        abort(400, "Missing longitude")

    data = request.get_json()
    instance = Farmer(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/farmers/<farmer_id>', methods=['PUT'], strict_slashes=False)
def put_farmer(farmer_id):
    """
    Updates a farmer
    """
    farmer = storage.get(Farmer, farmer_id)

    if not farmer:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'location', 'latitude', 'longitude']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(farmer, key, value)
    storage.save()
    return make_response(jsonify(farmer.to_dict()), 200)
#!/usr/bin/python3
"""
Methods that handle all default RESTFul API actions for FarmerProducts
"""
from models.farmer_product import FarmerProduct
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/farmer_products', methods=['GET'], strict_slashes=False)
def get_farmer_products():
    """
    Retrieves the list of all FarmerProduct objects
    or a specific FarmerProduct
    """
    all_farmer_products = storage.all(FarmerProduct).values()
    list_farmer_products = []
    for farmer_product in all_farmer_products:
        list_farmer_products.append(farmer_product.to_dict())
    return jsonify(list_farmer_products)


@app_views.route('/farmer_products/<farmer_product_id>', methods=['GET'], strict_slashes=False)
def get_farmer_product(farmer_product_id):
    """
    Retrieves a FarmerProduct 
    """
    farmer_product = storage.get(FarmerProduct, farmer_product_id)
    if not farmer_product:
        abort(404)

    return jsonify(farmer_product.to_dict())


@app_views.route('/farmer_products/<farmer_product_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_farmer_product(farmer_product_id):
    """
    Deletes a FarmerProduct Object
    """
    farmer_product = storage.get(FarmerProduct, farmer_product_id)

    if not farmer_product:
        abort(404)

    storage.delete(farmer_product)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/farmer_products', methods=['POST'], strict_slashes=False)
def post_farmer_product():
    """
    Creates a FarmerProduct
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'price' not in request.get_json():
        abort(400, description="Missing price")
    if 'product_id' not in request.get_json():
        abort(400, description="Missing product id")
    if 'farmer_id' not in request.get_json():
        abort(400, "Missing farmer id")

    data = request.get_json()
    instance = FarmerProduct(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
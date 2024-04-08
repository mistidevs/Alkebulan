#!/usr/bin/python3
""" objects that handle all default RestFul API actions for FarmerProducts """
from models.farmer_product import FarmerProduct
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


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
    """ Retrieves a farmer_product """
    farmer_product = storage.get(FarmerProduct, farmer_product_id)
    if not farmer_product:
        abort(404)

    return jsonify(farmer_product.to_dict())


@app_views.route('/farmer_products/<farmer_product_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/farmer_product/delete_farmer_product.yml', methods=['DELETE'])
def delete_farmer_product(farmer_product_id):
    """
    Deletes a farmer_product Object
    """

    farmer_product = storage.get(FarmerProduct, farmer_product_id)

    if not farmer_product:
        abort(404)

    storage.delete(farmer_product)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/farmer_products', methods=['POST'], strict_slashes=False)
@swag_from('documentation/farmer_product/post_farmer_product.yml', methods=['POST'])
def post_farmer_product():
    """
    Creates a farmer_product
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
#!/usr/bin/python3
""" Getting Statistics and Status of the API """

from models import storage
from models.admin import Admin
from models.consumer import Consumer
from models.farmer import Farmer
from models.farmer_product import FarmerProduct
from models.order import Order
from models.product import Product
from models.valid_login import ValidLogin
from models.invalid_login import InvalidLogin
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Status of API
    """
    return jsonify({"Alkebulan API": "Ready and Primed"})


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Status of API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """
    Retrieves the number of each catoegory of objects by type 
    """
    classes = [Admin, Consumer, Farmer, FarmerProduct, Order, Product, ValidLogin, InvalidLogin]
    names = ["admins", "consumers", "farmers", "farmer_products", "orders", "products", "valid_logins", "invalid_logins"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
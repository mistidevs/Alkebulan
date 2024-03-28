#!/usr/bin/python3
""" Index """

from models import storage
from models.admin import Admin
from models.consumer import Consumer
from models.farmer import Farmer
from models.farmer_product import FarmerProduct
from models.order import Order
from models.product import Product
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Admin, Consumer, Farmer, FarmerProduct, Order, Product]
    names = ["admins", "consumers", "farmers", "farmer_products", "orders", "products"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
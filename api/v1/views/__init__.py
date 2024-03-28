#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.consumers import *
from api.v1.views.products import *
from api.v1.views.admins import *
from api.v1.views.farmer_products import *
from api.v1.views.farmers import *
from api.v1.views.orders import *
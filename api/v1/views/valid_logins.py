#!/usr/bin/python3
"""
Methods that handle all default RESTFul API actions for ValidLogins
"""
from models.valid_login import ValidLogin
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/valid_logins', methods=['GET'], strict_slashes=False)
def get_valid_logins():
    """
    Retrieves the list of all ValidLogin objects
    or a specific ValidLogin
    """
    all_valid_logins = storage.all(ValidLogin).values()
    list_valid_logins = []
    for valid_login in all_valid_logins:
        list_valid_logins.append(valid_login.to_dict())
    return jsonify(list_valid_logins)


@app_views.route('/valid_logins/<valid_login_id>', methods=['GET'], strict_slashes=False)
def get_valid_login(valid_login_id):
    """
    Retrieves a ValidLogin
    """
    valid_login = storage.get(ValidLogin, valid_login_id)
    if not valid_login:
        abort(404)

    return jsonify(valid_login.to_dict())


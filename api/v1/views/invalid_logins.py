#!/usr/bin/python3
""" objects that handle all default RestFul API actions for InvalidLogins """
from models.invalid_login import InvalidLogin
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/invalid_logins', methods=['GET'], strict_slashes=False)
def get_invalid_logins():
    """
    Retrieves the list of all InvalidLogin objects
    or a specific InvalidLogin
    """
    all_invalid_logins = storage.all(InvalidLogin).values()
    list_invalid_logins = []
    for invalid_login in all_invalid_logins:
        list_invalid_logins.append(invalid_login.to_dict())
    return jsonify(list_invalid_logins)


@app_views.route('/invalid_logins/<invalid_login_id>', methods=['GET'], strict_slashes=False)
def get_invalid_login(invalid_login_id):
    """ Retrieves a invalid_login """
    invalid_login = storage.get(InvalidLogin, invalid_login_id)
    if not invalid_login:
        abort(404)

    return jsonify(invalid_login.to_dict())


#!/usr/bin/python3
"""Create a new view for State objects that
handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.user import User
from models import storage


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'])
def usersWithId(user_id=None):
    """Methods that retrieves all methods for users with id"""
    userId = storage.get(User, user_id)
    if userId is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(userId.to_dict())

    if request.method == 'DELETE':
        userId.delete()
        del userId
        return jsonify({}), 200

    if request.method == 'PUT':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        userId.save()
        return jsonify(userId.to_dict())


@app_views.route('/users/', methods=['POST', 'GET'])
def usersNoId():
    """Methods that retrieves all methods for users without id"""
    if request.method == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if request.get_json().get('name') is None:
            abort(400, 'Missing name')
        newUser = User(**request.get_json())
        newUser.save()
        return jsonify(newUser.to_dict()), 200

    if request.method == 'GET':
        allUser = storage.all(User)
        allUser = [allObject.to_dict() for allObject in allUser.values()]
        return jsonify(allUser)

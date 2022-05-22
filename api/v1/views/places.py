#!/usr/bin/python3
"""Create a new view for place objects that
handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.place import Place
from models import storage


@app_views.route('/places/<place_id>', methods=['GET', 'DELETE', 'PUT'])
def placesWithId(place_id=None):
    """Methods that retrieves all methods for places with id"""
    placeId = storage.get(Place, place_id)
    if placeId is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(placeId.to_dict())

    if request.method == 'DELETE':
        placeId.delete()
        del placeId
        return jsonify({}), 200

    if request.method == 'PUT':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        placeId.save()
        return jsonify(placeId.to_dict())


@app_views.route('/places/', methods=['POST', 'GET'])
def placesNoId():
    """Methods that retrieves all methods for places without id"""
    if request.method == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if request.get_json().get('name') is None:
            abort(400, 'Missing name')
        newPlace = Place(**request.get_json())
        newPlace.save()
        return jsonify(newPlace.to_dict()), 200

    if request.method == 'GET':
        allPlace = storage.all(Place)
        allPlace = [allObject.to_dict() for allObject in allPlace.values()]
        return jsonify(allPlace)

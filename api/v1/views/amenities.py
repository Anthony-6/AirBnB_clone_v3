#!/usr/bin/python3
"""Create a new view for State objects that
handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def amenitiesWithId(amenity_id=None):
    """Methods that retrieves all methods for amenities with id"""
    amenityId = storage.get(Amenity, amenity_id)
    if amenityId is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(amenityId.to_dict())

    if request.method == 'DELETE':
        amenityId.delete()
        del amenityId
        return jsonify({}), 200

    if request.method == 'PUT':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        amenityId.save()
        return jsonify(amenityId.to_dict())


@app_views.route('/amenities/', methods=['POST', 'GET'])
def statesNoId():
    """Methods that retrieves all methods for amenities without id"""
    if request.method == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if request.get_json().get('name') is None:
            abort(400, 'Missing name')
        newAmenity = Amenity(**request.get_json())
        newAmenity.save()
        return jsonify(newAmenity.to_dict()), 200

    if request.method == 'GET':
        allAmenity = storage.all(Amenity)
        allAmenity = [allObject.to_dict() for allObject in allAmenity.values()]
        return jsonify(allAmenity)

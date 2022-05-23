#!/usr/bin/python3
"""Create a new view for State objects that
handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.place import Place
from models.city import City
from models.state import State
from models import storage


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'],
                 strict_slashes=False)
def placeWithId(city_id=None):
    """Methods that retrieves all methods for states with id"""
    cityId = storage.get(City, city_id)
    transformers = request.get_json()
    if request.method == 'GET':
        if cityId is None:
            return abort(404)
        for city in storage.all(City).values():
            if city.id == city_id:
                list_place = [place.to_dict() for place in city.places]
        return jsonify(list_place.to_dict())

    if request.method == 'POST':
        if cityId is None:
            return abort(404)
        if transformers is None:
            return abort(404, 'Not a JSON')
        if transformers.get('user_id'):
            return abort(400, 'Missing user_id')
        if transformers.get('name'):
            return abort(400, 'Missing name')
        newCity = City(**transformers)
        newCity.save()
        return jsonify(newCity.to_dict, 201)


@app_views.route('/places/<places_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def placesId(places_id):
    """Methods that retrieves all methods for place without id"""
    placeId = storage.get(Place, places_id)
    transformers = request.get_json()
    if request.method == 'DELETE':
        if Place is None:
            return abort(404)
        placeId.delete()
        storage.save()
        return jsonify({})

    if request.method == 'PUT':
        if placeId is None:
            return abort(404)
        if transformers is None:
            return abort(404, 'Not a JSON')
        toIgnore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
        for key, value in transformers.items():
            if value not in toIgnore:
                setattr(placeId, key, value)
        placeId.save()
        return jsonify(placeId.to_dict()), 200

    if request.method == 'GET':
        allPlace = storage.all(Place)
        place = [allObject.to_dict() for allObject in allPlace.values()]
        return jsonify(place)

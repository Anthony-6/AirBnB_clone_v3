#!/usr/bin/python3
"""
This is the module for cities
"""

from api.v1.views import app_views
from flask import request, abort, jsonify
from models.state import State
from models import storage


@app_views.route("/states/<state_id>/cities", methods=["GET"])
def state_all_cities(state_id):
    """Retrieves all the cities of a given state_id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    all_cities = [city.to_json() for city in state.cities]
    return jsonify(all_cities)


@app_views.route("/cities/<city_id>", methods=["GET"])
def one_city(city_id):
    """Retrieves one city of a given city_id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({})


@app_views.route("/states/<state_id>/cities", methods=["POST"])
def create_one_city(state_id):
    """Creates one city tied with the given state_id based on the JSON body"""
    try:
        r = request.get_json()
    except:
        r = None
    if r is None:
        return "Not a JSON", 400
    if 'name' not in r.keys():
        return "Missing name", 400
    s = storage.get("State", state_id)
    if s is None:
        abort(404)
    c = City(**r)
    c.state_id = state_id
    c.save()
    return jsonify(c.to_json()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"])
def update_one_city(city_id):
    """Updates one city tied with the given state_id based on the JSON body"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    try:
        r = request.get_json()
    except:
        r = None
    if r is None:
        return "Not a JSON", 400
    for k in ("id", "created_at", "updated_at", "state_id"):
        r.pop(k, None)
    for k, v in r.items():
        setattr(city, k, v)
    city.save()
    return jsonify(city.to_json()), 200

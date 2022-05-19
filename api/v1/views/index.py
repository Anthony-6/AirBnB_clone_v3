#!/usr/bin/python
from api.v1.views import app_views
from flask import jsonify
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status')
def status():
    stat = {"status": "OK"}
    return jsonify(stat)

@app_views.route('api/v1/stats')
def countstorage():
    classes = {"Amenity": models.storage.count(Amenity),
               "City": models.storage.count(City),
               "Place": models.storage.count(Place),
               "Review": models.storage.count(Review),
               "State": models.storage.count(State),
               "User": models.storage.count(User)}
    return jsonify(classes)

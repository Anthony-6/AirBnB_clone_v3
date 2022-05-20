#!/usr/bin/python
from api.v1.views import app_views
from flask import jsonify
from models import storage
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

@app_views.route('/stats')
def countstorage():
    classes = {"amenity": storage.count(Amenity),
               "city": storage.count(City),
               "place": storage.count(Place),
               "review": storage.count(Review),
               "state": storage.count(State),
               "user": storage.count(User)}
    return jsonify(classes)

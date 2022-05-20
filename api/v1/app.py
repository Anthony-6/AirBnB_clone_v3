#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tearitdown(exception):
    """This method remove the current SQLAlchemy Session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """This method handle error 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    if getenv('HBNB_API_HOST') and getenv('HBNB_API_PORT') is None:
        app.run(host='0.0.0.0', port='5000')
    else:
        app.run(host=getenv('HBNB_API_HOST'), port=getenv('HBNB_API_PORT'))

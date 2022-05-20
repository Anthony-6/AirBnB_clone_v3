#!/usr/bin/python3
"""comment"""
from api.v1.views import app_views
from flask import request, abort

@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def statesWithId(state_id):
    """comment"""

@app_views.route('/states/', methods=['POST', 'GET'])
def statesNoId():
    """comment"""
    if request.methods == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if request.get_json().get('name') is None:
            abort(400, 'Missing name')

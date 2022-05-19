#!/usr/bin/python
from api.v1.views import app_views
import json

@app_views.route('/status')
def status():
    stat = {"status": "OK"}
    return json.loads(stat)

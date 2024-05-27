#!/usr/bin/python3
""" Defines interface for index"""

from api.v1.views import app_views
import json


@app_views.route('/status')
def get_status():
    """checks status of server"""
    return json.loads('{"status": "OK"}')

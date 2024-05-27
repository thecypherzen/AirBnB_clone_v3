#!/usr/bin/python3
""" Defines interface for index"""

from api.v1.views import app_views
from flask import jsonify
import models
from models import storage

@app_views.route('/status', strict_slashes=False)
def get_status():
    """checks status of server"""
    return jsonify('{"status": "OK"}')

@app_views.route('/stats', strict_slashes=False)
def get_models_stats():
    """retrieves the number of each objects by type"""
    res = f"""
          'amenities': '{storage.count(models.amenity.Amenity)}',
          'cities'   : '{storage.count(models.city.City)}',
          'places'   : '{storage.count(models.place.Place)}',
          'reviews'  : '{storage.count(models.review.Review)}',
          'states'   : '{storage.count(models.state.State)}',
          'users'    : '{storage.count(models.user.User)}'
          """
    return jsonify(res)

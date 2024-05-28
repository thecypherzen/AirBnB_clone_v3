#!/usr/bin/python3
"""Creates and manages our app"""

from api.v1.views import app_views
from flask import Flask, g, json
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception):
    """Tears down the storage"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """Handles 404 errors in app to return JSON"""
    return json.dumps({"error": "Not found"}, indent=2) + '\n', 404

@app.errorhandler(400)
def wrong_data(e):
    """Handles all wrong data related errors"""
    res = {"error": e.description}
    return json.dumps(res, indent=2) + '\n', 400


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST') or "0.0.0.0",
        port=getenv('HBNB_API_PORT') or 5000,
        threaded=True
    )

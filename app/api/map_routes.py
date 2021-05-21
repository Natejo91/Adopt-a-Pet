from flask import Blueprint, jsonify
import os


map_routes = Blueprint('map', __name__)

@map_routes.route('')
def get_map_api():
    '''
    Get the google map api key from .env
    '''
    mapKey = os.environ.get('GOOGLE_API_KEY')
    return jsonify(mapKey)

from flask import Blueprint, jsonify
from app.models import db, Breed


breed_routes = Blueprint('breeds', __name__)


@breed_routes.route('/<int:id>')
def get_breed(id):
    '''
    Get one animals breed
    '''
    breed = Breed.query.get(id)
    return breed.to_dict()

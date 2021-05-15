from flask import Blueprint, jsonify
from app.models import db, Shelter


shelter_routes = Blueprint('shelters', __name__)


@shelter_routes.route('')
def get_shelters():
    '''
    Get all shelters in database
    '''

    shelters = Shelter.query.all()
    return jsonify([shelter.to_dict() for shelter in shelters])


@shelter_routes.route('/<int:id>')
def get_shelter(id):
    '''
    Get a specific shelter from the database
    '''

    shelter = Shelter.query.get(id)
    return jsonify([shelter.to_dict()])

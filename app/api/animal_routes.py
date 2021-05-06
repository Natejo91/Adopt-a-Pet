from flask import Blueprint, jsonify
from app.models import db, Animal


animal_routes = Blueprint('animals', __name__)


@animal_routes.route('/')
def get_animals():
    '''
    Get all animals in database
    '''
    animals = Animal.query.all()
    return jsonify([animal.to_dict() for animal in animals])


@animal_routes.route('/<int:id>', methods=['POST'])
def get_animal(id):
    '''
    Get a specific animal from the database
    '''
    animal = Animal.query.get(id)
    return animal.to_dict()

#NEED TO RESEARCH ABOUT POST FOR SHELTER ROUTE
# @animal_routes.route('/<int:id>')
# def post_form_shelter():
#     animal = Animal.query.get(id)
#     need to post shelter adoption form here.


@animal_routes.route('/<int:id>', methods=['DELETE'])
def remove_animal(id):
    '''
    Delete an animal from the database
    '''
    animal = Animal.query.get(id)
    db.session.delete(animal)
    db.session.commit()
    return jsonify{'Animal has been adopted!'}

from flask import Blueprint, jsonify
from app.models import db, Animal, Shelter


animal_routes = Blueprint('animals', __name__)


@animal_routes.route('')
def get_animals():
    '''
    Get all animals in database
    '''
    animals = Animal.query.all()
    return jsonify([animal.to_dict() for animal in animals])


@animal_routes.route('/<int:id>')
def get_animal(id):
    '''
    Get a specific animal from the database
    '''
    animal = Animal.query.get(id)

    shelter = Shelter.query.get(animal.shelter_id)

    result = {}
    result["animal"] = [animal.to_dict()]
    result["shelter"] = [shelter.to_dict()]
    return result


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
    return 'Animal has been adopted!'

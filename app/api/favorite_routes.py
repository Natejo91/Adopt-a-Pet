from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user, login_user
from app.models import db, User, Favorite_Animal, Animal
from app.forms import SignUpForm

favorite_routes = Blueprint('favorite', __name__);



@favorite_routes.route('')
def get_Favorites():
    '''
    Return a users favorite pets
    '''

    userId = current_user.id
    favorite_animals = []
    for animal in current_user.favorite_animals:
        favorite_animals.append(Animal.query.get(animal.animal_id).to_dict())

    return jsonify(favorite_animals)


@favorite_routes.route('', methods=['POST'])
def post_favorite_animal():
    '''
    Add a new animal to a users favorites
    '''
    animalId = request.form['animalId']
    userId = current_user.id

    new_favorite_animal = Favorite_Animal(
        user_id = userId,
        animal_id = animalId
    )

    db.session.add(new_favorite_animal)
    db.session.commit()

    return jsonify(new_favorite_animal.animal_id)


@favorite_routes.route('/<int:animalId>', methods=['DELETE'])
def delete_favorite_animal(animalId):
    '''
    Remove an animal from a users favorites
    '''

    userId = current_user.id
    favorite_animal = Favorite_Animal.query.filter_by(user_id=userId, animal_id=animalId).first()
    db.session.delete(favorite_animal)
    db.session.commit()

    return jsonify(animalId)

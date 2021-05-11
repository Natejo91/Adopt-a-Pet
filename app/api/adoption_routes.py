from flask import Blueprint, jsonify, request
from flask_login import current_user
from app.models import db, Adoption

adoption_routes = Blueprint('adoptions', __name__)


@adoption_routes.route('', methods=['POST'])
def post_adoption():
    '''
    Post a users message about an animal
    '''
    userId = current_user.id
    animalId = request.form['animalId']

    new_adoption = Adoption(
        user_id = userId,
        animal_id = animalId,
        message = request.form['message']
    )

    db.session.add(new_adoption)
    db.session.commit()

    return new_adoption.to_dict()

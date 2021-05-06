from flask import Blueprint, jsonify
from app.models import Breed, Animal


search_routes = Blueprint('search', __name__)


@search_routes.route('/<string:squery>')
def search(squery):
    '''
    Does search by breed or by type and returns those animals
    '''

    search_result = {
        'animals_by_type': [],
        'animals_by_breed': []
    }

    animal_types = Animal.query.filter(Animal.type.ilike(f'%{squery}%')).all()

    breed = Breed.query.filter(Breed.name.ilike(f'%{squery}%')).first()
    breedDict = breed.to_dict()
    breedId = breedDict['id']
    animal_breeds = Animal.query.filter_by(breed_id=breedId).all()


    search_result['animals_by_type'] = [animal.to_dict() for animal in animal_types]
    search_result['animals_by_breed'] = [animal.to_dict() for animal in animal_breeds]

    return search_result

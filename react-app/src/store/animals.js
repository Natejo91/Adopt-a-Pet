const GET_ANIMALS = 'animal/GET_ALL_ANIMALS';
const GET_ONE_ANIMAL = 'animal/GET_ONE_ANIMAL';

const loadAll = animals => ({
    type: GET_ANIMALS,
    payload: animals
})

const loadOne = animal => ({
    type: GET_ONE_ANIMAL,
    payload: animal
})


export const getAnimals = () => async dispatch => {
    const response = await fetch('/api/animals');

    if (response.ok) {
        const animals = await response.json();
        dispatch(loadAll(animals))
        return animals
    }
}

export const getOneAnimal = (animalId) => async dispatch => {
    const response = await fetch(`/api/animals/${animalId}`)

    if (response.ok) {
        const animal = await response.json();
        dispatch(loadOne(animal))
        return animal
    }
}


const initialState = {}


export default function animalReducer(state = initialState, action) {
    switch(action.type) {
        case GET_ANIMALS:
                return {
                    "animals": action.payload
                }
        case GET_ONE_ANIMAL:
                return {
                    "animal": action.payload.animal,
                    "shelter": action.payload.shelter
                }
        default:
            return state
    }
}

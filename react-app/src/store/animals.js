const GET_ANIMALS = 'animal/GET_ALL_ANIMALS';

const load = animals => ({
    type: GET_ANIMALS,
    payload: animals
})


export const getAnimals = () => async dispatch => {
    const response = await fetch('/api/animals');

    if (response.ok) {
        const animals = await response.json();
        dispatch(load(animals))
        return animals
    }
}

export const getOneAnimal = (animalId) => async dispatch => {
    const response = await fetch(`/api/animals${animalId}`)

    if (response.ok) {
        const animal = await response.json();
        dispatch(load(animal))
        return animal
    }
}


const initialState = []



export default function animalReducer(state = initialState, action) {
    switch(action.type) {
        case GET_ANIMALS:
            return action.payload.id = [...action.payload]
        default:
            return state
    }
}

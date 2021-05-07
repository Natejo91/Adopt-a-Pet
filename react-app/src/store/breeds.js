const GET_BREED = 'breed/GET_BREED';
const REMOVE_BREED = 'breed/REMOVE_BREED';


const load = breed => ({
    type: GET_BREED,
    payload: breed
})

const remove = () => ({
    type: REMOVE_BREED
})


export const getBreed = (breedId) => async dispatch => {
    const response = await fetch(`/api/breeds/${breedId}`)

    if (response.ok) {
        const breed = await response.json();
        dispatch(load(breed))
    }
}

const initialState = {}

export const removeBreeds = () => async dispatch => {
        dispatch(remove())
}


export default function breedReducer(state = initialState, action) {
    switch(action.type) {
        case GET_BREED:
            return {
                "breed": action.payload
            }
        case REMOVE_BREED:
            return { "breed": null}
        default:
            return state
    }
}

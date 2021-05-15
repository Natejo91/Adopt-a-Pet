const GET_SHELTERS = 'shelter/GET_SHELTERS';

const load = shelters => ({
    type: GET_SHELTERS,
    payload: shelters
})


export const getShelters = () => async dispatch => {
    const response = await fetch('/api/shelters');

    if (response.ok) {
        const shelters = await response.json();
        dispatch(load(shelters))
    }
}

export const getOneShelter = (shelterId) => async dispatch => {
    const response = await fetch(`/api/shelters/${shelterId}`)

    if (response.ok) {
        const shelter = await response.json();
        dispatch(load(shelter))
    }
}


const initialState = {}


export default function shelterReducer(state = initialState, action) {
    switch(action.type) {
        case GET_SHELTERS:
            return {
                "shelters": action.payload
            }
        default:
            return state
    }
}

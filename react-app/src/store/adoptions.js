const POST_ADOPTION = 'adoption/POST_ADOPTION';


const postAdoption = (adoption) => ({
    type: POST_ADOPTION,
    payload: adoption
})


export const addAdoption = (userId, animalId, message) => async dispatch => {
    const formData = new FormData();
    formData.append('animalId', animalId)
    formData.append('userId', userId)
    formData.append('message', message)

    const response = await fetch('/api/adoptions', {
        method: "POST",
        body: formData
    })

    if (response.ok) {
        const data = await response.json();
        dispatch(postAdoption(data))
    }
}


const initialState = {
    adoptions: []
}


export default function adoptionReducer(state = initialState, action) {
    switch(action.type) {
        case POST_ADOPTION:
            return { ...state, adoptions: action.payload}
        default:
            return state
    }
}

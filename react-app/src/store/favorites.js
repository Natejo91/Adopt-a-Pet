import { addFavorite, removeFavorite } from '../store/session';
const GET_FAVORITES = 'favorite/GET_FAVORITES';
const GET_ONE_FAV = 'favorite/GET_ONE_FAV';


const loadAll = favorites => ({
    type: GET_FAVORITES,
    payload: favorites
})

const loadOne = favorite => ({
    type: GET_ONE_FAV,
    payload: favorite
})

export const getUserFavorites = () => async dispatch => {
    const response = await fetch(`/api/favorites`);

    if (response.ok) {
        const favorites = await response.json();
        dispatch(loadAll(favorites))
        return favorites
    }
}

// need to figure out adding favorites
export const addUserFavorite = (animalId, userId) => async dispatch => {
    const formData = new FormData();
    formData.append('animalId', animalId);
    formData.append('userId', userId)

    const response = await fetch(`/api/favorites`, {
        method: "POST",
        body: formData
    })

    if (response.ok) {
        const data = await response.json();
        dispatch(addFavorite(data))
    }
}

export const removeUserFavorite = ( animalId ) => async (dispatch) => {
    const response = await fetch(`/api/favorites/${animalId}`, {
        method: "DELETE"
    })

    if (response.ok) {
        const data = await response.json();
        dispatch(removeFavorite(data))
    }
}


const initialState = {
    favorites: []
}


export default function favoriteReducer(state = initialState, action) {
    switch(action.type) {
        case GET_FAVORITES:
            return { ...state, favorites: action.payload}
        default:
            return state
    }
}

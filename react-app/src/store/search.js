const LOAD_SEARCH = 'search/LOAD_SEARCH';

const load = search => ({
    type: LOAD_SEARCH,
    payload: search
})

export const getSearch = (search) => async dispatch => {
    const response = await fetch(`/api/search/${search}`);

    if (response.ok) {
        const search = await response.json();
        dispatch(load(search))
        return search
    }
}


const initialState = {
    'animals_by_type': [],
    'animals_by_breed': []
}


const searchReducer = (state = initialState, action) => {
    switch(action.type) {
        case LOAD_SEARCH:
            return {
                'animals_by_type': [...action.payload.animals_by_type],
                'animals_by_breed': [...action.payload.animals_by_breed]
            }
        default:
            return state;
    }
}

export default searchReducer;

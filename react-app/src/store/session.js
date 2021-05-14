// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const ADD_FAVORITE = "session/ADD_FAVORITE";
const REMOVE_FAVORITE = "session/REMOVE_FAVORITE";


const setUser = (user) => ({
    type: SET_USER,
    payload: user
})

const removeUser = () => ({
    type: REMOVE_USER
})

export const addFavorite = (animalId) => ({
    type: ADD_FAVORITE,
    payload: animalId
})

export const removeFavorite = (animalId) => ({
    type: REMOVE_FAVORITE,
    payload: animalId
})


// thunks
export const authenticate = () => async (dispatch) => {
    const response = await fetch('/api/auth/', {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(setUser(data))
    }
}

export const login = (email, password) => async (dispatch) => {
    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            password
        })
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(setUser(data));
        return data;
    } else {
        // throw Error(response.statusText);
    }
}

export const logout = () => async (dispatch) => {
    const response = await fetch("/api/auth/logout", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(removeUser());

    } else {
        throw Error(response.statusText);
    }
};


export const signUp = (firstname, lastname, email, image, zipcode, password) => async (dispatch)=> {
    const formData = new FormData();
    formData.append('first_name', firstname)
    formData.append('last_name', lastname)
    formData.append('email', email)
    formData.append('image', image)
    formData.append('password', password)
    formData.append('zipcode', zipcode)


    const response = await fetch("/api/auth/signup", {
        method: "POST",
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(setUser(data));
    } else {
        throw Error(response.statusText);
    }
}

// reducer

const initialState = { user: null };

// useSelector(state => state.session.user)

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_USER:
            return { user: action.payload };
        case REMOVE_USER:
            return { user: null };
        case ADD_FAVORITE:
            state.user.favorite_animals[action.payload] = action.payload
            return { ...state }
        case REMOVE_FAVORITE:
            delete state.user.favorite_animals[action.payload]
            return { ...state }
        default:
            return state;
    }
}

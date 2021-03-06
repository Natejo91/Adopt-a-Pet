import {createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from 'redux-thunk';
import session from './session'
import search from './search';
import animals from './animals';
import shelters from './shelters';
import breeds from './breeds';
import favorites from './favorites';
import adoptions from './adoptions';
import modals from './modals';


const rootReducer = combineReducers({
    session,
    search,
    animals,
    shelters,
    breeds,
    favorites,
    adoptions,
    modals
});

let enhancer;

if (process.env.NODE_ENV === 'production') {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require('redux-logger').default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;

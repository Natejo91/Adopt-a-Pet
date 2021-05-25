import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import { ModalProvider } from './context/Modal';
import { BrowserRouter } from 'react-router-dom';
import { authenticate } from './services/auth';

import configureStore from './store';
import * as sessionActions from './store/session';
import * as searchActions from './store/search';
import * as animalActions from './store/animals';
import * as breedActions from './store/breeds';
import * as adoptionActions from './store/adoptions';
import * as modalActions from './store/modals';

const store = configureStore();

if (process.env.NODE_ENV !== 'production') {
  authenticate();

  window.store = store;
  window.sessionActions = sessionActions;
  window.searchActions = searchActions;
  window.animalActions = animalActions;
  window.breedActions = breedActions;
  window.adoptionActions = adoptionActions;
  window.modalActions = modalActions;

}

function Root() {
  return (
    <Provider store={store}>
      <ModalProvider>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </ModalProvider>
    </Provider>
  )
}



ReactDOM.render(
  <React.StrictMode>
    <Root/>
  </React.StrictMode>,
  document.getElementById('root')
);

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Home from './Router';
import { Provider } from 'react-redux';
import { fetchLocalUser } from './store/actions/fetchLocalUser';
import store from './store';

store.dispatch(fetchLocalUser());

ReactDOM.render(
  <Provider store={ store }>
    <Home />
  </Provider>
, document.getElementById('root'));


import { getTokens } from './getTokens';
import { AUTHORIZE_USER, SET_LOGIN_STATUS } from '../constants';

export const loginAction = (state, props) => {
  return (dispatch, getState) => {
    if(!state.username || !state.password) {
      alert('Both username and password are required');
      return;
    }
    getTokens(state, props, dispatch, getState);
  }
}

export const setTokens = (data) => {
  return {
    type: AUTHORIZE_USER,
    payload: {
      data,
    }
  }
}


export const logOutAction = (props) => 
  { return (dispatch, getState) => {
    localStorage.clear();
    const action = setTokens({});
    dispatch(action);
    const loginStatusAction = {
      type: SET_LOGIN_STATUS,
      payload: {
        loginStatus: 'logedout',
      }
    };
    dispatch(loginStatusAction);
    props.history.push('/login');
  }
}
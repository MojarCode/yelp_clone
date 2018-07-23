import { SERVER_URL, SET_LOCAL_USER } from '../constants';
import { validateTokens } from './validateTokens';

export const fetchUserInfo = (props) => {
  return (dispatch, getState) => {

    const state = getState();
    validateTokens(state, dispatch, props)
    .then(response => {
      const headers = ({
        Authorization: `Bearer ${getState().tokens.access}`,
      });
      const config = {
        method: 'GET',
        headers,
      }
      return fetch(SERVER_URL + 'me/', config);
    })
    .then(response => {
      console.log(response);
      return response.json();
    })
    .then(data => {
      if (!data.ok){
        console.log(data);
        dispatch(setLocalUser(data))
      }
    })
  }
}

const setLocalUser = (data) => {
  return {
    type: SET_LOCAL_USER,
    payload: {
      data,
    }
  }
}
import { logOutAction, setTokens } from './userActions';
import { SERVER_URL } from '../constants';

export const validateTokens = (state, dispatch, props) => {
  const access = state.tokens.access;
  //checking access token for validity
  const accessBody = {
    token: access,
  };
  const accessHeaders = new Headers({
    'content-type': 'application/json',
  });
  const accessConfig = {
    method: 'POST',
    body: JSON.stringify(accessBody),
    headers: accessHeaders,
  }
  const refreshHeaders = new Headers({
    'content-type': 'application/json',
  });
  return fetch(SERVER_URL + 'auth/token/verify/', accessConfig)
    .then(response => {
      // console.log(response);
      if(response.status===401){
        // checking refresh token
        const refresh = state.tokens.refresh;
        // using let because it's gonna be reassigned later
        let refreshBody = {
          token: refresh,
        };  
        const refreshConfig = {
          method: 'POST',
          body: JSON.stringify(refreshBody),
          headers: refreshHeaders,
        };
        return fetch(SERVER_URL + 'auth/token/verify/', refreshConfig);
      }
      return;
    })
    .then(response => {
      if (response === undefined) {
        return;
      }
      // console.log(response);
      if (response.status===200){
        const refreshBody = {
          refresh: state.tokens.refresh,
        }
        const refreshConfig = {
          method: 'POST',
          body: JSON.stringify(refreshBody),
          headers: refreshHeaders,
        };
        return fetch(SERVER_URL + 'auth/token/refresh/', refreshConfig);
      }
      else {
        dispatch(logOutAction(props));
        return;
      }
    })
    .then(response => {
      if (response === undefined) {
        return;
      }
      // console.log(response);
      return response.json()
    })
    .then(data => {
      if (data === undefined) {
        return;
      }
      console.log(data);
      const tokens = {
        refresh: state.tokens.refresh,
        access: data.access, 
      }
      const action = setTokens(tokens);
      dispatch(action);
      localStorage.setItem('tokens', JSON.stringify(tokens));
    })
}
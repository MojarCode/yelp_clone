import { getTokens } from './getTokens';
import { SERVER_URL } from '../constants';

export const signupAction = (state, props) => {
  return (dispatch, getState) => {
    if(!state.email) {
      alert('You should fill the email field');
      return;
    }
    const body = {
      email: state.email,
    }
    const headers = new Headers({
      'content-type': 'application/json',
    })
    const config = {
      method: 'POST',
      body: JSON.stringify(body),
      headers: headers,
    }
    // const myUrl = SERVER_URL + 'registration/';
    fetch(SERVER_URL + 'registration/', config)
      .then(response => {
        // console.log(response);
        if (response.status === 200) {
          props.history.push('/signup_message');
        }
        else if (response.status === 400) {
          alert('Bad e-mail format or user with this email already exists.');
        }
        return response.json();
      })
  }
}

export const validationSubmitAction = (state, props) => {
  return (dispatch, getState) => {
    if (!state.email || !state.code || !state.username || !state.location || !state.password || !state.password_repeat) {
      alert('Not all fields filled');
    }
    else {
      const body = {
        email: state.email,
        code: state.code,
        username: state.username,
        location: state.location,
        password: state.password,
        password_repeat: state.password_repeat,
      }
      const headers = new Headers({
        'content-type': 'application/json',
      })
      const config = {
        method: 'POST',
        body: JSON.stringify(body),
        headers,
      }
      fetch(SERVER_URL + 'registration/validation/', config)
      .then(response => {
        // console.log(response);
        return response.json()
      })
      .then(data => {
        // console.log(data);
        const body = {
          username: state.username,
          password: state.password,
        }
        getTokens(body, props, dispatch, getState);
      })
    }
  }
}
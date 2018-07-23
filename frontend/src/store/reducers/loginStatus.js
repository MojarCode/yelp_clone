import { SET_LOGIN_STATUS } from '../constants';

export const loginStatus = (state={loginStatus: 'logedout'}, action) => {
  switch (action.type) {
    case SET_LOGIN_STATUS: {
      return action.payload;
    }
    default: 
      return state;
  }
}
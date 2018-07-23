import { AUTHORIZE_USER } from '../constants';

export const tokens = (state={}, action) => {
  switch(action.type){
    case AUTHORIZE_USER: {
      return action.payload.data;
    }
    default:
      return state;
  }
}
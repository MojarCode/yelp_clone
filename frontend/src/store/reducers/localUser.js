import { SET_LOCAL_USER } from '../constants';

export const localUser = (state={}, action) => {
  switch(action.type){
    case SET_LOCAL_USER: {
      return action.payload.data;
    }
    default:
      return state;
  }
}
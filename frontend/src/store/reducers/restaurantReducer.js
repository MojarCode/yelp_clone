import { GET_RESTAURANTS } from "../constants";

const initialState = {};

export const restaurantReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_RESTAURANTS:
      console.log("in the restaurantContentReducer, case: 'GET_RESTAURANTS'");
      const newState = { ...state };
      console.log(action.payload.restaurants);
      return action.payload.restaurants;
    default:
      return state;
  }
};

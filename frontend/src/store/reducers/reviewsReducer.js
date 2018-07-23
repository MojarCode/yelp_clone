import { GET_REVIEWS } from "../constants";

export const reviewsReducer = (state = {}, action) => {
  switch (action.type) {
    case GET_REVIEWS:
      return action.payload.reviews;
    default:
      return state;
  }
};
import { SERVER_URL } from "../constants";
import { GET_RESTAURANTS } from "../constants";

const postRestaurant = restaurants => ({
  type: GET_RESTAURANTS,
  payload: { restaurants }
});

export const fetchRestaurant = restaurants => dispatch => {
  // const restaurants = getState().restaurants;
  const headers = new Headers({
    "content-type": "application/json"
  });
  console.log("in the fetchRestaurant");
  const config = {
    method: "GET",
    headers: headers
  };
  fetch(`${SERVER_URL}/restaurants`, config)
    .then(res => res.json())
    .then(data => {
      console.log("In da promise", data);
      dispatch(postRestaurant(data));
    });
};

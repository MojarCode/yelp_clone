import { SERVER_URL } from '../constants';
import { GET_REVIEWS } from '../constants';


const getReviews = (reviews) => ({
  type: GET_REVIEWS,
  payload: { reviews }
});



export const reviewAction = (state) => {
    return (dispatch, getState) => {
      const headers = new Headers({
        'content-type': 'application/json',
      })
      const config = {
        method: 'GET',
        headers: headers,
      }
      console.log("Before Fetch")
      fetch(SERVER_URL + 'reviews/restaurant/1/', config)
        .then(response => {
            return response.json();
        }).then(reviews =>{
          const newState = { ...state }
          reviews.forEach(element => {
            newState[element.id]= element
          });
          dispatch(getReviews(newState))
        })
    }
  }
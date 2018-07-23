import React, { Component } from "react";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { fetchRestaurant } from "../../store/actions/fetchRestaurant";

import styled from "styled-components";

import "./food-example.jpeg";

const StyledCard = styled.section`
  display: -webkit-flex;
  display: flex;
  -webkit-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-flex-direction: row;
  flex-direction: row;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
  -webkit-flex-flow: row wrap;
  flex-flow: row wrap;
  -webkit-align-content: flex-end;
  align-content: flex-end;
  text-shadow: 1px -2px 4px #000000;
  border-top: 5px solid #f27c3e;
  border-left: 1px solid #000;
  border-right: 1px solid #000;
  border-bottom: 1px solid #000;
  border-radius: 5px;
  width: 25%;
  color: white;
`;

const ratingChanged = newRating => {
  console.log(newRating);
};

class RestaurantCard extends Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    if (this.props) {
      console.log("CompoonentDidMount");
      this.props.dispatch(fetchRestaurant(this.state));
    } else {
      console.log("Loading...");
    }
  }

  render() {
    console.log("In da card!");
    return (
      <div className="RestaurantCard-main-container">
        <StyledCard>
          <div className="RestaurantCard-list-container">
            <img
              className="RestaurantCard-img-top"
              src={"food-example.jpeg"}
              alt="restaurant-review"
            />
            <div className="RestaurantCard-card-container">
              {/* <h4 className="RestaurantCard-title">{props.restaurant.name}</h4> */}
              <h6 className="RestaurantCard-address">
                {/* {props.restaurant.address} */}
              </h6>
              <p className="RestaurantCard-description">
                {/* {props.restaurant.content} */}
              </p>
            </div>

            <div className="RestaurantCard-footer">
              <div className="RestaurantCard-clearfix">
                <div className="" />
                <div className="RestaurantCard-rating">
                  {/* {props.restaurant.rating} */}
                </div>
              </div>
            </div>
          </div>
        </StyledCard>

        <div className="RestaurantCard-restaurant-container" />
        <div className="Card-container" />
      </div>
    );
  }
}

// access the store - to retrieve / access it
const mapStateToProps = (state, props) => {
  console.log("state", state.restaurantReducer[0]);
  // state.restaurantReducer.map();
  if (state) {
    console.log("state", state);
  }
  return {
    restaurant: state.restaurantReducer[0]
  };
};

export default withRouter(connect(mapStateToProps)(RestaurantCard));


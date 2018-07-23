import React, { Component } from "react";
import { connect } from "react-redux";
import { withRouter, Link } from "react-router-dom";
import { reviewAction } from "../../store/actions/review";

class Review extends Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.props.dispatch(reviewAction(this.state));
    // if(this.props.reviews){
    //     console.log('CompDidMout state')
    //     console.log(this.state)

    // }
  }
  render() {
    if (this.props.reviews) {
      console.log("this.props.review");
      console.log(this.props.reviews);
    } else {
      console.log("Loading");
    }
    return (
      <div className="Review-container">
        {this.props.reviews.map(review => {
          <div>{review.content}</div>;
        })}
      </div>
    );
  }
  handleFetchReviews = e => {
    e.preventDefault();
    this.props.dispatch(reviewAction(this.state));
  };
}
const mapStateToProps = (state, props) => {
  if (state && state.reviewsReducer) {
    console.log(state.reviewsReducer);
    const reviews = [];
    Object.values(state.reviewsReducer).map(review => {
      reviews.push(review);
    });
    console.log(reviews);

    return {
      reviews
    };
  }
};

export default withRouter(connect(mapStateToProps)(Review));

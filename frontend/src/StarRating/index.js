import React, { Component } from "react";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

import styled from "styled-components";
import ReactStars from "react-stars";
import React from "react";
import { render } from "react-dom";


class StarRating extends Component {
  constructor(props) {
    super(props);
    this.state = {  };
  }
  render() {
    <ReactStars
        count={5}
        onChange={ratingChanged}
        size={24}
        color2={'#ffd700'}
      />,
 
    document.getElementById('where-to-render')
    return (
      
    );
  }
}

export default StarRating;
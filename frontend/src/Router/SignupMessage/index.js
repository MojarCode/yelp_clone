import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import './index.css';

class SignupMessage extends Component {

  componentDidMount  = () => {
    setTimeout(() => {
      this.props.history.push('/');
    }, 10000);
  }

  render() {
    return (
      <div className='SignupMessage-container'>
          <h1>Registration</h1>
          <p className='SignupMessage-message'>
          Thanks for your registration.<br/>
Our hard working monkeys are preparing a digital message called E-Mail that will be sent to you soon. Since monkeys arent good in writing the message could end up in you junk folder. Our apologies for any inconvienience.
        </p>
      </div>
    )
  }
}

const mapStateToProps = (state, props) => {
  return {

  }
}

export default withRouter(connect(mapStateToProps)(SignupMessage));
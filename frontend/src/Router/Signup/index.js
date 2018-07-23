import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import './index.css';
import { signupAction } from '../../store/actions/signup';

class Signup extends Component {

  constructor(props){
    super(props);

    this.state = {
      email: '',
    }
  }

  handleEmailChange = (e) => {
    this.setState({
      email: e.currentTarget.value,
    })
  }

  handleSubmit = (e) => {
    e.preventDefault();
    const action = signupAction(this.state, this.props);
    this.props.dispatch(action);
    this.setState({
      username: '',
      password: '',
      email: '',
    })
  }


  render() {
    return (
      <div className='Signup-container'>
        <form className='Signup-container-form' onSubmit={ this.handleSubmit }>
          <h1>Registration</h1>
          <input 
            type='text' 
            placeholder='E-Mail address'
            value={ this.state.email }
            onChange={ this.handleEmailChange }
          />
          <button>Register</button>
        </form>
      </div>
    )
  }
}

const mapStateToProps = (state, props) => {
  return {

  }
}

export default withRouter(connect(mapStateToProps)(Signup));
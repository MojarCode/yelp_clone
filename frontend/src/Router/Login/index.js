import React, { Component } from 'react';
// import { validationSubmitAction } from '../../store/actions/signup';
import { connect } from 'react-redux';
import { loginAction } from '../../store/actions/userActions';
import './index.css';

var queryString = require('simple-query-string');

class Login extends Component {

  constructor (props) {
    super(props);

    this.parsed = queryString.parse(this.props.location.search);

    this.state = {
      username: '',
      password: '',
    }
  }

  handleUsernameChange = (e) => {
    this.setState({
      username: e.currentTarget.value,
    })
  }

  handlePasswordChange = (e) => {
    this.setState({
      password: e.currentTarget.value,
    })
  }

  handleLoginSubmit = (e) => {
    e.preventDefault();
    const action = loginAction(this.state, this.props);
    this.props.dispatch(action);
    this.setState({
      username: '',
      password: '',
    })
  }

  render() {
    return (
      <div className='Login-container'>
        <form className='Login-form' onSubmit={ this.handleLoginSubmit }>
        <h1>Login</h1>
          <div className='Login-formfields-container'>
            <input 
              type='text' 
              placeholder='Username'
              value={ this.state.username }
              onChange={ this.handleUsernameChange }
            />
            <input 
              type='password' 
              placeholder='Password'
              value={ this.state.password }
              onChange={ this.handlePasswordChange }
            />
          </div>
          <button onClick={ this.handleValidationSubmit }>Login</button>
        </form>
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  return {

  }
}

export default connect(mapStateToProps)(Login);
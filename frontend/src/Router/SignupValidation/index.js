import React, { Component } from 'react';
import { validationSubmitAction } from '../../store/actions/signup';
import { connect } from 'react-redux';
import './index.css';

var queryString = require('simple-query-string');
class SignupValidation extends Component {

  constructor (props) {
    super(props);

    this.parsed = queryString.parse(this.props.location.search);

    this.state = {
      email: this.parsed.email,
      code: this.parsed.code,
      username: '',
      location: '',
      password: '',
      password_repeat: '',
    }
  }

  handleEmailChange = (e) => {
    this.setState({
      email: e.currentTarget.value,
    })
  }

  handleCodeChange = (e) => {
    this.setState({
      code: e.currentTarget.value,
    })
  }

  handleUsernameChange = (e) => {
    this.setState({
      username: e.currentTarget.value,
    })
  }

  handleLocationChange = (e) => {
    this.setState({
      location: e.currentTarget.value,
    })
  }

  handlePasswordChange = (e) => {
    this.setState({
      password: e.currentTarget.value,
    })
  }

  handlePasswordRepeatChange = (e) => {
    this.setState({
      password_repeat: e.currentTarget.value,
    })
  }

  handleValidationSubmit = (e) => {
    e.preventDefault();
    this.props.dispatch(validationSubmitAction(this.state, this.props));
    this.setState({
      email: '',
      code: '',
      username: '',
      location: '',
      password: '',
      password_repeat: '',
    })
  }

  render() {
    console.log(this.props);
    return (
      <div className='SignupValidation-container'>
        <form className='SignupValidation-form' onSubmit={ this.handleValidationSubmit }>
        <h1>Verification</h1>
          <div className='SignupValidation-formfields-container'>
            <input 
              type='text' 
              placeholder='E-Mail address'
              value={ this.state.email }
              onChange={ this.handleEmailChange }
            />
            <input 
              type='text' 
              placeholder='Validation code'
              value={ this.state.code }
              onChange={ this.handleCodeChange }
            />
            <input 
              type='text' 
              placeholder='Username'
              value={ this.state.username }
              onChange={ this.handleUsernameChange }
            />
            <input 
              type='text' 
              placeholder='Location'
              value={ this.state.location }
              onChange={ this.handleLocationChange }
            />
            <input 
              type='password' 
              placeholder='Password'
              value={ this.state.password }
              onChange={ this.handlePasswordChange }
            />
            <input 
              type='password' 
              placeholder='Password repeat'
              value={ this.state.password_repeat }
              onChange={ this.handlePasswordRepeatChange }
            />
          </div>
          <button onClick={ this.handleValidationSubmit }>Finish registration</button>
        </form>
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  return {

  }
}

export default connect(mapStateToProps)(SignupValidation);
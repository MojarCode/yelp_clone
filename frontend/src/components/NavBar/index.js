import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link }  from 'react-router-dom';
import { logOutAction } from '../../store/actions/userActions';
import { fetchUserInfo } from '../../store/actions/fetchUserInfo';
import { SET_LOGIN_STATUS } from '../../store/constants'
import logo from './logo.svg'

import './index.css';

import Review from '../Review'


class NavBar extends Component {

  constructor(props) {
    super(props);

    this.state = {
      loginStatus: 'login',
    }
  }

  navigate = (e) => {
    const activeLi = document.getElementsByClassName('Navbar-nav-li-active')[0];
    activeLi.classList.remove('Navbar-nav-li-active');
    e.currentTarget.classList.add('Navbar-nav-li-active');
  }

  handleSignUp = (e) => {
    e.preventDefault();
    this.props.history.push('/signup');
  }

  handleLogin = (e) => {
    e.preventDefault();

    // if (this.props.loginStatus === 'logedin') {
    //   this.props.dispatch(logOutAction(this.props));
    // }
    // else {
    this.props.history.push('/login');
    // }
  }

  handleLogout = (e) => {
    e.preventDefault();
    this.props.dispatch(logOutAction(this.props));
    this.props.history.push('/');
  }

  componentDidMount = () => {
    if (this.props.tokens.access) {
      const loginStatusAction = {
        type: SET_LOGIN_STATUS,
        payload: {
          loginStatus: 'logedin',
        }
      }
      this.props.dispatch(loginStatusAction);
    }
    this.props.dispatch(fetchUserInfo(this.props));
  }

  addCorrectButtons = () => {
    if (this.props.loginStatus === 'logedin') {
      return (
          <div className='NavBar-auth-container'>
            <button className='NavBar-auth-logout' onClick={ this.handleLogout }>Logout</button>
          </div>
      )
    }
    else if (this.props.loginStatus === 'logedout'){
      return (
        <div className='NavBar-auth-container'>
          <button className='NavBar-auth-signup' onClick={ this.handleSignUp }>Signup</button>
          <button className='NavBar-auth-login' onClick={ this.handleLogin }>Login</button>
        </div>
      )
    }
  }

  render() {
    console.log(this.props);
    return (
    
      <div className='NavBar-container'>
        <div className='NavBar-logo-container'>
          <img src={ logo } alt='Luna-logo'/>
          
        </div>
        <div className='NavBar-navigation-container'>
          <div className='Navbar-nav'>
            <ul>
              <li className='Navbar-nav-li-active' onClick={ this.navigate }><Link to='/'>Home</Link></li>
              <li onClick={ this.navigate }><Link to='/'>Search</Link></li>
              <li onClick={ this.navigate }><Link to='/'>Profile</Link></li>
              
            </ul>
          </div>
          {
            this.addCorrectButtons()
          }
          {/* <div className='NavBar-auth-container'>
            <button className='NavBar-auth-signup' onClick={ this.handleSignUp }>Signup</button>
            <button className='NavBar-auth-login'>Login</button>
            
          </div>
          
            <button className='NavBar-auth-login' onClick={ this.handleLogin }>{ this.state.loginStatus }</button>
          </div> */}
        </div>
        <Review />
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
  return {
    
    tokens: state.tokens,
    loginStatus: state.loginStatus.loginStatus,
    localUser: state.localUser
  }
}

export default withRouter(connect(mapStateToProps)(NavBar));
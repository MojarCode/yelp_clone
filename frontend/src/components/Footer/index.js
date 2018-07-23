import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link }  from 'react-router-dom';
import google_logo from './googleplus.svg';
import facebook_logo from './facebook.svg';
import instagram_logo from './instagram.svg';
import twitter_logo from './twitter.svg';

import './index.css';


class Footer extends Component {

  navigate = (e) => {
    
  }

  render() {
    return (
      <div className='Footer-container'>
        <div className='Footer-navigation-container'>
          <ul className='Footer-nav'>
            <li onClick={ this.navigate }><Link to='/'>About Us</Link></li>
            <li onClick={ this.navigate }><Link to='/'>Press</Link></li>
            <li onClick={ this.navigate }><Link to='/'>Blog</Link></li>
            <li onClick={ this.navigate }><Link to='/'>iOS</Link></li>
            <li onClick={ this.navigate }><Link to='/'>Android</Link></li>
          </ul>
          <div className='Footer-social-networks'>
            <Link to='/'><img src={ facebook_logo } alt='facebook-logo'/></Link>
            <Link to='/'><img src={ twitter_logo } alt='Luna-logo'/></Link>
            <Link to='/'><img src={ google_logo } alt='google_logo'/></Link>
            <Link to='/'><img src={ instagram_logo } alt='Luna-logo'/></Link>
          </div>
        </div>
        <div className='Footer-copyright'>&copy;Copyright Luna {new Date().getFullYear()}</div>
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
  return {

  }
}

export default withRouter(connect(mapStateToProps)(Footer));
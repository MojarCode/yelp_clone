import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';
import Signup from './Signup';
import Login from './Login';
import SignupMessage from './SignupMessage';
import NewRestaurant from './NewRestaurant';
import ScrollToTop from '../components/ScrollToTop';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import SignupValidation from './SignupValidation';

const Home = (props) => {
    return (
      <Router>
        <Switch>
          <ScrollToTop>
            <NavBar />
            <Route exact path="/" component={ App } />
            <Route exact path="/signup" component={ Signup } />
            {/* <Route exact path="/restaurant/:id" component={ Restaurant } /> */}

            <Route exact path="/signup_message" component={ SignupMessage } />
            <Route exact path="/registration/validation" component={ SignupValidation } />
            <Route exact path="/login" component={ Login } />
            <Route exact path="/new_restaurant" component={ NewRestaurant } />
            <Footer />
          </ScrollToTop>
        </Switch>
      </Router>
    )
}


export default Home;
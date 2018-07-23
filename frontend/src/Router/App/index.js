import React, { Component } from "react";
import "./index.css";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import Restaurant from "../../components/Restaurant";

class App extends Component {

  constructor (props) {
    super(props);

    this.state = {
      search: '',
    }
  }
  handleSearchChange = (e) => {
    this.setState({
      search: e.currentTarget.value,
    })
  }

  render() {
    console.log(this.props);
    return (

      <div className='App-container'>
        <div className='App-search-container'>
          <input 
            type='text' 
            placeholder='search...'
            value={ this.state.search }
            onChange={ this.handleSearchChange }
          />
          <button>Search</button>
        </div>
        {/*<Card />*/}
        <Restaurant />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  console.log(state);
  let localUser;
  if (Object.keys(state.localUser).length === 0 && state.localUser.constructor === Object) {
    localUser = '';
  }
  else {
    localUser = state.localUser;
  }
  return {
    tokens: state.tokens,
    loginStatus: state.loginStatus.loginStatus,
    localUser,
  }
}


export default withRouter(connect(mapStateToProps)(App));

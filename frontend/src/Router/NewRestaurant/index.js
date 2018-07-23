import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { countries } from '../../store/constants';
import { validate_form } from './helper.js';
import './index.css';

var rand = require("random-key");



class NewRestaurant extends Component {

  constructor(props){
    super(props);

    this.state = {
      name: { value: '', required: true },
      category: { value: '', required: true },
      country: { value: '', required: true },
      street: { value: '', required: true },
      city: { value: '', required: true },
      zip: { value: '', required: false },
      website: { value: '', required: false },
      phone: { value: '', required: true },
      email: { value: '', required: false },
      opening_hours: { value: '', required: true },
      price_level: { value: '', required: false },
      image: { value: '', required: false },
    }
  }

  handleNameChange = (e) => {
    this.setState({
      name: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }

  handleCountryChange = (e) => {
    this.setState({
      country: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }

  handleCategoryChange = (e) => {
    this.setState({
      category: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }

  handleStreetChange = (e) => {
    this.setState({
      street: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }

  handleCityChange = (e) => {
    this.setState({
      city: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }

  handleZipChange = (e) => {
    this.setState({
      zip: {
        value: e.currentTarget.value,
        required: false,
      }
    })
  }

  handleWebsiteChange = (e) => {
    this.setState({
      website: {
        value: e.currentTarget.value,
        required: false,
      }
    })
  }


  handlePhoneChange = (e) => {
    this.setState({
      phone: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }


  handleEmailChange = (e) => {
    this.setState({
      email: {
        value: e.currentTarget.value,
        required: false,
      }
    })
  }

  handleOpeningHoursChange = (e) => {
    this.setState({
      opening_hours: {
        value: e.currentTarget.value,
        required: true,
      }
    })
  }

  handlePriceLevelChange = (e) => {
    this.setState({
      price_level: {
        value: e.currentTarget.value,
        required: false,
      }
    })
  }

  handleSubmit = (e) => {
    e.preventDefault();
    const invalid_fields = validate_form(this.state);
    console.log(invalid_fields);
  }

  render() {
    return (
      <div className='NewRestaurant-container'>
        <form className='NewRestaurant-form' onSubmit={ this.handleSubmit }>
          <h1>Create new restaurant</h1>
          <div className='NewRestaurant-formfields-container'>
            <div className='NewRestaurant-formfields-fieldset'>
              <legend>Basic</legend>
              <div className='NewRestaurant-formfields-fieldset-inputs'>
                <div>
                  <label htmlFor='name'>Name<abbr title="required">*</abbr></label>
                  <input 
                    id='name'
                    type='text' 
                    value={ this.state.name.value }
                    onChange={ this.handleNameChange }
                  />
                </div>
                <div className='NewRestaurant-formfields-dropdown'>
                  <label htmlFor='category'>Category<abbr title="required">*</abbr></label>
                  <select name='Category' id='category' onChange={ this.handleCategoryChange } value={ this.state.category.value }>
                    {
                      Object.keys(this.props.categories).map(index => {
                        return <option key={ rand.generate(10) } value={ this.props.categories[index] }>{ this.props.categories[index] }</option>
                      })
                    }
                  </select>
                </div>
                <div className='NewRestaurant-formfields-dropdown'>
                  <label htmlFor='country'>Country<abbr title="required">*</abbr></label>
                  <select name='Country' id='country' onChange={ this.handleCountryChange } value={ this.state.country.value }>
                    {
                      Object.keys(countries).map(index => {
                        return <option key={ rand.generate(10) } value={ countries[index] }>{ countries[index] }</option>
                      })
                    }
                  </select>
                </div>
              </div>
            </div>
            <div className='NewRestaurant-formfields-fieldset'>
            <legend>Address</legend>
            <div className='NewRestaurant-formfields-fieldset-inputs'>
              <div>
                <label htmlFor='street'>Street<abbr title="required">*</abbr></label>
                <input 
                  id='street'
                  type='text' 
                  value={ this.state.street.value }
                  onChange={ this.handleStreetChange }
                />
              </div>
              <div>
                <label htmlFor='city'>City<abbr title="required">*</abbr></label>
                <input 
                  id='city'
                  type='text' 
                  value={ this.state.city.value }
                  onChange={ this.handleCityChange }
                />
              </div>
              <div>
                <label htmlFor='zip'>Zip</label>
                <input 
                  id='zip'
                  type='text' 
                  value={ this.state.zip.value }
                  onChange={ this.handleZipChange }
                />
              </div>
              </div>
            </div>
            <div className='NewRestaurant-formfields-fieldset'>
            <legend>Contact</legend>
            <div className='NewRestaurant-formfields-fieldset-inputs'>
              <div>
                <label htmlFor='website'>Website</label>
                <input 
                  id='website'
                  type='text' 
                  value={ this.state.website.value }
                  onChange={ this.handleWebsiteChange }
                />
              </div>
              <div>
                <label htmlFor='Phone'>Phone<abbr title="required">*</abbr></label>
                <input 
                  id='phone'
                  type='text' 
                  value={ this.state.phone.value }
                  onChange={ this.handlePhoneChange }
                />
              </div>
              <div>
                <label htmlFor='email'>Email</label>
                <input 
                  id='email'
                  type='text' 
                  value={ this.state.email.value }
                  onChange={ this.handleEmailChange }
                />
              </div>
              </div>
            </div>
            <div className='NewRestaurant-formfields-fieldset'>
            <legend>Details</legend>
            <div className='NewRestaurant-formfields-fieldset-inputs'>
              <div>
                <label htmlFor='opening_hours'>Opening hours<abbr title="required">*</abbr></label>
                <input 
                  id='opening_hours'
                  type='text' 
                  value={ this.state.opening_hours.value }
                  onChange={ this.handleOpeningHoursChange }
                />
              </div>
              <div className='NewRestaurant-formfields-dropdown'>
                <label htmlFor='price_level' onChange={ this.handlePriceLevelChange }>Price level</label>
                <select name='Price level' id='price_level'>
                  <option value='default'></option>
                  <option value='$'>$</option>
                  <option value='$$'>$$</option>
                  <option value='$$$'>$$$</option>
                </select>
              </div>
              <div>
                <label htmlFor='image'>Image</label>
                <div className='NewRestaurant-formfields-fileUploadContainer'>
                  <button className='NewRestaurant-formfields-fileUploadButton'>Choose a file...</button>
                  <input type="file" id="file" name="file" multiple accept=".jpg, .jpeg, .png"/>
                </div>
              </div>
              </div>
            </div>
          </div>
          <button 
            type='submit'
            className='NewRestaurant-form-submitButton'
          >
            Create
          </button>
        </form>
      </div>
    )
  }
}

const mapStateToProps = (state, props) => {
  const categories = ['', 'Pizzeria', 'Mexican', 'Burger place']
  return {
    categories,
  }
}

export default withRouter(connect(mapStateToProps)(NewRestaurant));
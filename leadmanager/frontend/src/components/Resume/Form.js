import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addResume, getResume } from '../../actions/resume';

export class Form extends Component {
  state = {
    name: '',
    label: '',
    picture: '',
    email: '',
    phone: '',
    degree: '',
    website: '',
    summary: '',
    address: '',
    postalCode: '',
    countryCode: '',
    region: '',
    profiles: []
  };

  static propTypes = {
    resume: PropTypes.array.isRequired,
    addResume: PropTypes.func.isRequired,
    getResume: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getResume();
  }

  onChange = e =>
    this.setState({
      [e.target.name]: e.target.value
    });

  onSubmit = e => {
    e.preventDefault();
    const {
      name,
      label,
      picture,
      email,
      phone,
      degree,
      website,
      summary,
      address,
      postalCode,
      countryCode,
      region,
      profiles: []
    } = this.state;
    const resume = {
      name,
      label,
      picture,
      email,
      phone,
      degree,
      website,
      summary,
      address,
      postalCode,
      countryCode,
      region,
      profiles: []
    };
    this.props.addResume(resume);
  };

  render() {
    const {
      name,
      label,
      picture,
      email,
      phone,
      degree,
      website,
      summary,
      address,
      postalCode,
      countryCode,
      region,
      profiles: []
    } = this.state;
    return (
      <div className='card card-body mt-4 mb-4'>
        <h2>Resume</h2>
        <form onSubmit={this.onSubmit}>
          <div className='form-group'>
            <label>Name</label>
            <input
              className='form-control'
              type='text'
              name='name'
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className='form-group'>
            <label>Email</label>
            <input
              className='form-control'
              type='email'
              name='email'
              onChange={this.onChange}
              value={email}
            />
          </div>
          <div className='form-group'>
            <label>Summary</label>
            <input
              className='form-control'
              type='text'
              name='summary'
              onChange={this.onChange}
              value={summary}
            />
          </div>
          <div className='form-group'>
            <button type='submit' className='btn btn-primary'>
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  resume: state.resume.resume
});

export default connect(
  mapStateToProps,
  { addResume, getResume }
)(Form);

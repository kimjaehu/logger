import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { logout } from '../../actions/auth';

export class Header extends Component {
  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  };

  render() {
    const { isAuthenticated, user } = this.props.auth;

    const authLinks = (
      <ul className='navbar-nav ml-auto mt-2 mt-lg-0'>
        <span className='navbar-text mr-3'>
          <strong>{user ? `Welcome [${user.username}]` : ''}</strong>
        </span>
        <li className='nav-item'>
          <button
            onClick={this.props.logout}
            className='btn btn-outline-primary'
          >
            logout
          </button>
        </li>
      </ul>
    );
    // <li className='nav-item'>
    //   <Link to='/register' className='nav-link'>
    //     register
    //   </Link>
    // </li>
    const guestLinks = (
      <ul className='navbar-nav ml-auto mt-2 mt-lg-0'>
        <li className='nav-item'>
          <Link to='/login' className='btn btn-outline-primary'>
            login
          </Link>
        </li>
      </ul>
    );

    return (
      <nav className='navbar navbar-expand-lg navbar-light bg-light'>
        <div className='container'>
<<<<<<< HEAD
          <a className='navbar-brand' href='#'>
            Logger
=======
          <a className='navbar-brand' href='/'>
            topilocal
>>>>>>> faff2e0cb8473feaf4e31982b398a580fab9c27f
          </a>
          <button
            className='navbar-toggler'
            type='button'
            data-toggle='collapse'
            data-target='#navbarNavAltMarkup'
            aria-controls='navbarNavAltMarkup'
            aria-expanded='false'
            aria-label='Toggle navigation'
          >
            <span className='navbar-toggler-icon' />
          </button>
          <div className='collapse navbar-collapse' id='navbarNavAltMarkup'>
            {isAuthenticated ? authLinks : guestLinks}
          </div>
        </div>
      </nav>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { logout }
)(Header);

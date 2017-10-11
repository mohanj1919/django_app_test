import React, { Component } from 'react'

export default function (ComposedComponent, Roles) {
  class Authentication extends Component {
    componentWillMount () {
      if (!this.props.ValidateUserToken() && !this.props.router.isActive('/login')) {
        this.props.router.push('/login')
      }
      var role = localStorage.getItem('logged_user_role')
      if (role) {
        if (!Roles.includes(role)) {
          this.props.router.push('/')
        }
      }
    }
    componentWillUpdate (nextProps) {
      if (!nextProps.authenticated && !this.props.router.isActive('/login')) {
        this.props.router.push('/login')
      }
    }

    render () {
      return <ComposedComponent {...this.props} />
    }
  }
  return Authentication
}

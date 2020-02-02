import React from 'react';
// import MuiAppBar from '@material-ui/core/AppBar';

import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap';
import './Navbar.css'
import logo from '../images/SocialLiteLogo.png'

export default class NavBar extends React.Component {
  constructor(props) {
    super(props);

    this.toggleNavbar = this.toggleNavbar.bind(this);
    this.state = {
      collapsed: true
    };
  }

  toggleNavbar() {
    this.setState({
      collapsed: !this.state.collapsed
    });
  }
  render() {
    return (
      <div>
        <Navbar className="top-bar" color="faded" light>
          <img class="logo" src={logo} alt="logo" />
        
          <NavbarBrand href="/" className="mr-auto">SOCIAL  LITE</NavbarBrand>
          <NavbarToggler onClick={this.toggleNavbar} className="mr-2" />
        </Navbar>
        <Collapse isOpen={!this.state.collapsed} navbar>
            <Nav navbar>
              <NavItem>
                <NavLink href="/">Home</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="/login">Login</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="/about">About</NavLink>
              </NavItem>
            </Nav>
          </Collapse>
      </div>
    );
  }
}
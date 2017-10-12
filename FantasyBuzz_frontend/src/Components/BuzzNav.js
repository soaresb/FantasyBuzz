import React from 'react';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap';
var navTextStyle = {
  color: 'white'
};
export default class Example extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {
    return (
      <div>
        <Navbar color="dark" light expand="md" >
          <NavbarBrand href="/" style={navTextStyle}>FantasyBuzz</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar >

              <NavItem>
                <NavLink href="/QB" style={navTextStyle}>QBs</NavLink>
              </NavItem>
              <NavItem >
                <NavLink href="/RB" style={navTextStyle} >RBs</NavLink>
              </NavItem>
              <NavItem >
                <NavLink href="/WR" style={navTextStyle} >WRs</NavLink>
              </NavItem>
              <NavItem >
                <NavLink href="/TE" style={navTextStyle} >TEs</NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Navbar>
      </div>
    );
  }
}

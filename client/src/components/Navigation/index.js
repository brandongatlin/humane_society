import React from "react";
import { NavLink } from "react-router-dom";
import { Nav, NavItem } from 'reactstrap';

// Depending on the current path, this component sets the "active" class on the appropriate navigation link item
const Navigation = () => {

  return (
    <Nav className="navbar navbar-expand-lg navbar-light bg-light">
      <NavLink className="navbar-brand" to="/">
        BHS
      </NavLink>
      <div>
        <ul className="navbar-nav">
          <NavItem>
            <NavLink
              to="/pets"
              className={
                window.location.pathname === "/pets"
                  ? "nav-link active"
                  : "nav-link"
              }
            >
              Our Pets
            </NavLink>
          </NavItem>
          <NavItem>
            <NavLink
              to="/lost"
              className={window.location.pathname === "/lost" ? "nav-link active" : "nav-link"}
            >
              Lost Pets
            </NavLink>
          </NavItem>
          {/* <li className="nav-item">
            <Link
              to="/search"
              className={window.location.pathname === "/search" ? "nav-link active" : "nav-link"}
            >
              Search
            </Link>
          </li> */}
        </ul>
      </div>
    </Nav>
  );
}

export default Navigation;

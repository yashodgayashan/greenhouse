import React, { Component } from 'react';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

import Site from "./sites/Site";
import Greenhouse from "./greenhouse/Greenhouse";

class App extends Component {
    state = {  }
    render() { 
        return ( 
          <div>
              <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
                  <Navbar.Brand href="/">HND Agro</Navbar.Brand>
                  <Navbar.Collapse id="responsive-navbar-nav" className="justify-content-end">
                      <Nav className="mr-auto">
                          <Nav.Link href="/sites">Sites</Nav.Link>
                          <Nav.Link href="/greenhouses">Greenhouses</Nav.Link>
                      </Nav>
                  </Navbar.Collapse>
              </Navbar>
              <br/>
              <Router>
                  <div>
                      <Switch>
                          <Route path="/sites">
                              <Site />
                          </Route>
                          <Route path="/greenhouses">
                              <Greenhouse />
                          </Route>
                      </Switch>
                  </div>
              </Router>
          </div>
        );
    }
}
 
export default App;

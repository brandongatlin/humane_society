import React from 'react';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Button } from 'reactstrap';

import Home from './components/Home';


function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/pets">Pets</Link>
            </li>
            <li>
              <Link to="/lost">Lost Pets</Link>
            </li>
          </ul>
        </nav>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/pets">
            <h1>PETS</h1>
          </Route>
          <Route path="/lost">
            <Button color="danger">LOST</Button>
          </Route>
          <Route path="*">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;

import React from 'react';
import {ReactQueryDevtools} from 'react-query-devtools';

import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";

import Navigation from './components/Navigation';
import NoMatch from './components/NoMatch';

import Home from './components/Home';
import Pets from './components/Pets';
import Lost from './components/Lost';


function App() {
  return (
    <>
    <Router>
      <div>
        <Navigation />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/pets" component={Pets} />
          <Route exact path="/lost" component={Lost} />
          <Route component={NoMatch} />          
        </Switch>
      </div>
    </Router>
    {process.env.NODE_ENV !== 'production' ? <ReactQueryDevtools initialIsOpen={false}/> : null}
    </>
  );
}

export default App;

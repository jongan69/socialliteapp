import React, { Component } from 'react';

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import About from '../components/About';
import Dashboard from '../components/Dashboard';
import Login from '../components/Login';
import Home from '../containers/Home';
import withAuthentication from '../containers/withAuthentication';

import './App.css';

class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/dashboard" component={withAuthentication(Dashboard)} />
          <Route path="/about" component={About} />
        </Switch>
      </Router>
    );
  }
}

export default App;

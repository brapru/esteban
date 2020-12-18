import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import icon from '../assets/esteban_load.svg';

const Hello = () => {
  return (
    <div>
      <div className="Hola">
        <img className="icon" alt="icon" src={icon} />
      </div>
      <div className="text">
        <h1 className="hola">hóla.</h1>
      </div>
    </div>
  );
};

export default function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" component={Hello} />
      </Switch>
    </Router>
  );
}

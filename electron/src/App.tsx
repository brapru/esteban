import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import icon from '../assets/esteban_load.svg';
import styles from './constants/styles.css'

const Hello = () => {
  return (
    <div>
      <div className="Hola">
        <img alt="icon" src={icon} />
      </div>
      <div className="hola">
        <h1>hóla</h1>
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

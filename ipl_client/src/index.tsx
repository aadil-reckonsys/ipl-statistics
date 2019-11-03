import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import * as serviceWorker from './serviceWorker';
import MainPage from 'pages/main/main';
import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css'

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path='/search' render={props => <MainPage {...props} />}/>
      <Redirect from="/" to="/search" />
    </Switch>
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

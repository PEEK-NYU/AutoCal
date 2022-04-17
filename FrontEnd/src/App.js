import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Home from './pages/Home/Home';
import Test from './pages/Test/Test';
import Rooms from './pages/Rooms/Rooms';
import Users from './pages/Users/Users';
import LogReg from './pages/LogReg/LogReg';
import Event from './pages/Event/Event';
import Account from './pages/Account/Account';
import Search from './pages/Search/Search';

import {backendurl} from './config';

import './App.css';

function App() {
  console.log(backendurl);
  return (
    <div className="root">
      <div className="content">
        <Router>
          <Switch>

            <Route exact={true} path={'/'}>
              <Home />
            </Route>

            <Route exact={true} path={'/test'}>
              <Test />
            </Route>

            <Route exact={true} path={'/rooms'}>
              <Rooms />
            </Route>

            <Route exact={true} path={'/users'}>
              <Users />
            </Route>

            <Route exact={true} path={'/logreg'}>
              <LogReg />
            </Route>

            <Route exact={true} path={'/events_edit'}>
              <Event />
            </Route>

            <Route exact={true} path={'/account'}>
              <Account />
            </Route>

            <Route exact={true} path={'/search'}>
              <Search />
            </Route>

          </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;

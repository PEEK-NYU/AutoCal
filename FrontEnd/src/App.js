import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Home from './pages/Home/Home';
import Test from './pages/Test/Test';
import Login from './pages/Login/Login';
import Register from './pages/Register/Register';
import Event from './pages/Event/Event';
import Account from './pages/Account/Account';
import Search from './pages/Search/Search';
import Import from './pages/Import/Import';
import { TokenContextProvider } from './components/TokenContext/TokenContext';

import {backendurl} from './config';

import './App.css';


function App() {
  console.log(backendurl);
  return (
    <TokenContextProvider>
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

              <Route exact={true} path={'/login'}>
                <Login />
              </Route>

              <Route exact={true} path={'/register'}>
                <Register />
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

              <Route exact={true} path={'/import'}>
                <Import />
              </Route>

            </Switch>
          </Router>
        </div>
      </div>
    </TokenContextProvider>
  );
}

export default App;

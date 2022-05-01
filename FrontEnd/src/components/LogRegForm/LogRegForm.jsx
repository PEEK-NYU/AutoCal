import React, {useState} from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import {backendurl} from '../../config';
import './LogRegForm.css';


export default function LogRegForm({setToken}){

  const [username, setUserName] = useState('');
  const [password, setPassword] = useState(0);  
  const [error, setError] = useState(undefined);

  const handleLogin = (e) => { 
    e.preventDefault();
    //axios.post(`${backendurl}/users/login/${username}/${password}`)
    console.log(`${backendurl}/admin/hello`)
    axios.get(`${backendurl}/admin/hello`)
      .then((response) => {
        console.log(response.data);
        //triiger navigation to home
        //set token to user id
        //setRefresh(refresh + 1);
      })
      .catch(error => {
        setError(error);
        console.log(error);
      })
  }

  return (
    <div className="logregform">

      {error && (
        <div className="login-error-box">
          <p>{error.toString()}</p>
        </div>
      )}

      <form onSubmit={e=>{e.preventDefault()}}>
        <label>
          <p>Username</p>
          <input type="text" onChange={e => setUserName(e.target.value)}/>
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={e => setPassword(e.target.value)}/>
        </label>
        <div>
          <button type="submit" onClick={handleLogin}>Submit</button>
        </div>
      </form>
    </div>
  )
}

// // Add in the PropType from the new prop and destructure the props object to pull out the setToken prop
// LogRegForm.propTypes = {
//   setToken: PropTypes.func.isRequired
// }
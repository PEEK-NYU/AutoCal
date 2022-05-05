import React, {useState} from 'react';
import axios from 'axios';
import { useTokenContext } from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';


import {backendurl} from '../../config';
import './LogRegForm.css';


export default function LogRegForm(){

  const history = useHistory();
  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');  
  const [error, setError] = useState(undefined);
  const {token, setToken} = useTokenContext(); //token, setToken

  const handleLogin = (e) => { 
    e.preventDefault();
    axios.get(`${backendurl}/users/login/${username}/${password}`)
      .then((response) => {
        console.log(response.data);
        setToken(response.data);
        history.push('/');
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

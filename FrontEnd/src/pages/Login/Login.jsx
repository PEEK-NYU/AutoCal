import React, {useState} from 'react';
import axios from 'axios';
import {useTokenContext} from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';

import {backendurl} from '../../config';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';

import './login.css'


export default function Login(){

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
        setToken(response.data); //set token to user id
        history.push('/'); //navigate to home
      })
      .catch(error => {
        console.log(error);
        setError(error);
      })
  }

  return (
    <div className="Login">
        <PageTitle
          text="Login"
        />

      {error && (
          <div className="login-error-box">
            <p>{error.toString()}</p>
          </div>
      )}

      <div className="login-form">
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

      <NavButton text={'Go Back Home'} subpath={'/'}/>

    </div>
  );
};

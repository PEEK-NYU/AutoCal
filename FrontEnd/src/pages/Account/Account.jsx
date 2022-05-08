import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { useTokenContext } from '../../components/TokenContext/TokenContext';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import Inputbox from '../../components/Inputbox/Inputbox'

import { backendurl } from '../../config';

export default function Account(){

  const {token, setToken} = useTokenContext(); //token, setToken
  const [newemail, setNewemail] = useState('');
  const [newusrname, setNewusrname] = useState('');
  const [newpasswrd, setNewpasswrd] = useState('');
  const [email, setEmail] = useState('');
  const [usrname, setUsrname] = useState('');
  const [passwrd, setPasswrd] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get(`${backendurl}/users/get/${token}`)
      .then((response) => {
        console.log(response.data);
        setEmail(response.data.email);
        setUsrname(response.data.username);
        setPasswrd(response.data.password);
      })
      .catch(error => {
        console.log(error);
        setError(error);
      });
  }, [])

  return (
    <div className="content">
      <div className="account-header">
        <PageTitle
          text="Account"
        />
      </div>

      <div className="setNewemail">
      <p>Email Address: {email}</p>
        {/* <button onClick={() => setNewemail(!newemail)}>Set New Email</button>
        {newemail && (
          <form onSubmit={e=>{e.preventDefault()}}>
            <Inputbox label={''} placeholder={'New Email Address'}/>
            <input type="submit" value="Update" /> 
          </form>
        )} */}
      </div>

      <div className="setNewusrname">
        <p>User Name: {usrname}</p>
        {/* <button onClick={() => setNewusrname(!newusrname)}>Set New User Name</button>
        {newusrname && (
          <form onSubmit={e=>{e.preventDefault()}}>
            <Inputbox label={''} placeholder={'New User Name'}/>
            <input type="submit" value="Update" /> 
          </form>
        )} */}
      </div>

      <div className="setNewpasswrd">
        <p>Password: {passwrd}</p>
        {/* <button onClick={() => setNewpasswrd(!newpasswrd)}>Set New Password</button>
        {newpasswrd && (
          <form onSubmit={e=>{e.preventDefault()}}>
            <Inputbox label={''} placeholder={'New Password'}/>
            <Inputbox label={''} placeholder={'Confirm New Password'}/>
            <input type="submit" value="Update" /> 
          </form>
        )} */}
      </div>

      <div>
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>
    </div>
  );
};
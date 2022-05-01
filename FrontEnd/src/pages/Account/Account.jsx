import React, {useState} from 'react';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import Inputbox from '../../components/Inputbox/Inputbox'


export default function Account(){

  const [newemail, setNewemail] = useState(false);
  const [newusrname, setNewusrname] = useState(false);
  const [newpasswrd, setNewpasswrd] = useState(false);


  return (
    <div className="content">
      <div className="account-header">
        <PageTitle
          text="Account"
        />
      </div>

      <div className="Info">
        <label>Email Address:</label>
        <p>----</p>
        <label>User Name:</label>
        <p>----</p>
        <label>Password:</label>
        <p>----</p>
      </div>

      <div className="setNewemail">
        <button onClick={() => setNewemail(!newemail)}>Set New Email</button>
        {newemail && (
          <form onSubmit={e=>{e.preventDefault()}}>
            <Inputbox label={''} placeholder={'New Email Address'}/>
            <input type="submit" value="Update" /> 
          </form>
        )}
      </div>

      <div className="setNewusrname">
        <button onClick={() => setNewusrname(!newusrname)}>Set New User Name</button>
        {newusrname && (
          <form onSubmit={e=>{e.preventDefault()}}>
            <Inputbox label={''} placeholder={'New User Name'}/>
            <input type="submit" value="Update" /> 
          </form>
        )}
      </div>

      <div className="setNewpasswrd">
        <button onClick={() => setNewpasswrd(!newpasswrd)}>Set New Password</button>
        {newpasswrd && (
          <form onSubmit={e=>{e.preventDefault()}}>
            <Inputbox label={''} placeholder={'New Password'}/>
            <Inputbox label={''} placeholder={'Confirm New Password'}/>
            <input type="submit" value="Update" /> 
          </form>
        )}
      </div>

      <div>
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>
    </div>
  );
};
import React, {useEffect, useState} from 'react';
import {useHistory} from 'react-router-dom';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import Inputbox from '../../components/Inputbox/Inputbox'
import ColorPicker from '../../components/ColorPicker'
import DateInput from '../../components/DateInput'


export default function Account(){

  const [newpasswrd, setNewpasswrd] = useState(false);


  return (
    <div className="content">
      <div className="account-header">
        <PageTitle
          text="Account"
        />
      </div>
      <div className="Info">
        <label>Account Name:</label>
        <p>----</p>
        <label>Password</label>
        <p>----</p>
      </div>
      <button onClick={() => setNewpasswrd(!newpasswrd)}>Set New Password</button>


      {newpasswrd && (
        <form>
          <Inputbox label={''} placeholder={'New Password'}/>
          <Inputbox label={''} placeholder={'Confirm New Password'}/>
          <input type="submit" value="Update" /> 
        </form>
      )}

      <div>
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>
    </div>
  );
};
import React from 'react';
import {useHistory} from 'react-router-dom';

import RoomItem from '../../components/RoomItem/RoomItem';
import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import LogRegForm from '../../components/LogRegForm/LogRegForm'

export default function LogReg(){
  return (
    <div className="content">
      <div className="login-header">
        <PageTitle
          text="Login"
        />
      </div>
      <LogRegForm/>
      <NavButton text={'Go Back Home'} subpath={'/'}/>

    </div>
  );
};
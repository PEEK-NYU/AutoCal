import React from 'react';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';
import LogRegForm from '../../components/LogRegForm/LogRegForm';

export default function LogReg(){
  return (
    <div className="content">
      <div className="login-header">
        <PageTitle
          text="Login/Register"
        />
      </div>
      <LogRegForm/>
      <NavButton text={'Go Back Home'} subpath={'/'}/>

    </div>
  );
};
import React from 'react';
import {useHistory} from 'react-router-dom';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import Inputbox from '../../components/Inputbox/Inputbox'
import ColorPicker from '../../components/ColorPicker'
import DateInput from '../../components/DateInput'


export default function LogReg(){
  return (
    <div className="content">
      <div className="event-header">
        <PageTitle
          text="Event"
        />
      </div>
      <form>
        <div className="input-container">
          <Inputbox label={''} placeholder={'Event Name'}/>
        </div>
        <div className="input-container">
          <ColorPicker label={''}/>
        </div>
        <div className="input-container">
          <Inputbox label={''} placeholder={'Location'}/>
        </div>
        <div className="input-container">
          <DateInput label={'Start'}/>
        </div>
        <div className="input-container">
          <DateInput label={'End'}/>
        </div>
        <div>
          <Inputbox label={''} placeholder={'Event Description'}/>
        </div>
        <div className="button-container">
          <input type="submit" value="Update" /> 
        </div>
      </form>
      <div className="Edit Event">
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>
    </div>
  );
};
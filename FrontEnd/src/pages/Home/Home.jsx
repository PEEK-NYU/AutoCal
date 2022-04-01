import React from 'react';
import {useHistory} from 'react-router-dom';
import NavButton from '../../components/NavButton/NavButton'

export default function Home(){
  return (
    <div className="content">
      <h1>AutoCal</h1>
      <p> CALENDER PLANNER FOR ALL </p>
      <NavButton text={'View All Rooms'} subpath={'/rooms'}/>
      <NavButton text={'View All Users'} subpath={'/users'}/>
      <NavButton text={'Login/Register'} subpath={'/logreg'}/>
      <NavButton text={'Event Edit'} subpath={'/events_edit'}/>
    </div>
  );
};


import React from 'react';
import NavButton from '../../components/NavButton/NavButton'

export default function Test(){
  return (
    <div className="content">
      <h1>AutoCal</h1>
      <p> CALENDER PLANNER FOR ALL </p>
      <NavButton text={'View All Rooms'} subpath={'/rooms'}/>
      <NavButton text={'View All Users'} subpath={'/users'}/>
      <NavButton text={'Login/Register'} subpath={'/logreg'}/>
      <NavButton text={'Event Edit'} subpath={'/events_edit'}/>
      <NavButton text={'Account Settings'} subpath={'/account'}/>
      <NavButton text={'Event Search'} subpath={'/search'}/>
    </div>
  );
};

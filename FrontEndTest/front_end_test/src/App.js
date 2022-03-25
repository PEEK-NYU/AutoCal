import React from 'react'; //always required

import {useState} from 'react'; //for setting values
import {useEffect} from 'react'; //for fetching data?
import axios from 'react';

import Button from './Components/Button';
import Login from './Components/Login';
import DateInput from './Components/DateInput';
import ColorPicker from './Components/ColorPicker';
import Inputbox from './Components/Inputbox';

export default function App() {


  return (

    <div>
      <Login/>
      <Inputbox label={"An Inputbox"} placeholder={"default"}/>
      <ColorPicker/>
      <DateInput label={"Start:"}/>
      <Button text={"Upload"}/>
    </div>
  )

}



import React from 'react'; //always required

import {useState} from 'react'; //for setting values
import {useEffect} from 'react'; //for fetching data?
import axios from 'react';

import Button from './Components/Button';
import Login from './Components/Login';

export default function App() {


  return (

    <div>
      <Button text={"Upload"}/>
      <Login/>
    </div>
  )

}



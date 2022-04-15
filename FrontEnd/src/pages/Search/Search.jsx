import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import EventItem from '../../components/EventItem/EventItem';
import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'

import {backendurl} from '../../config';

import './Search.css';

export default function Search() {
  return (
    <div className="content">
      <PageTitle text={'Event Search'}/>
      <NavButton text={'Go Back Home'} subpath={'/'}/>
    </div>
  )
}

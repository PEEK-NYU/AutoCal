import React, {useState} from 'react';
import axios from 'axios';
import {useTokenContext} from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';

import {backendurl} from '../../config';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';


export default function Import(){

  return (
    <PageTitle text="Import" />
  );
};

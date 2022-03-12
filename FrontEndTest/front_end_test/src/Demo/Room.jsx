import React from 'react';
import {useEffect} from 'react';

/*
Component Definition File, 27:42 talks about passing by props
*/


export default function Room({roomName, numUsers}){

	return (
		<div>
			<h1> Room </h1>
			<p> {roomName} </p>
			<p> {numUsers} </p>
		</div>
	)

}
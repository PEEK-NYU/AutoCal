import React from 'react';
//import {useEffect} from 'react';
import {useHistory} from 'react-router-dom';
//import './NavButton.css';


export default function NavButton({text,subpath}){
	const history = useHistory();

	function navigateToPage(path) {
		history.push(path);
	}

	return (
	    <button
	      onClick={() => navigateToPage(subpath)}
	      className="button-nav"
	    >
	      {text}
	    </button>
	)

}
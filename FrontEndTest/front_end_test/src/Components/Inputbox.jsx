import React from 'react';


export default function Inputbox({label, placeholder}){

	return (
	    <div class="sub-main">
	    	<label for={label}>{label}</label>
	      	<input type="text" id="phone" name="phone" placeholder={placeholder}/>
	    </div>
	)

}
import React from 'react';
//<label for={label}>{label}</label>
//<input type="text" id="phone" name="phone" placeholder={placeholder}/>
export default function Inputbox({label, placeholder}){

	return (
	    <div class="sub-main">
	    	<label>{label}</label>
	      	<input type="text" placeholder={placeholder}/>
	    </div>
	)

}
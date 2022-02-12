import React from 'react'; //always required


import {useState} from 'react'; //for setting values


export default function App(){
  const [counter, setCounter] = useState(0); // A State Variable
  // const [Var, update_func] = useState(def_val_Var);
  // Var, function exposed to set the Var, default val for Var
  // update_func_name is just an alias for the function, like import random as rd
  // Cor: <button onClick={incCounter}>

  const [aString, setAString] = useState('');
  // Cor: <button onClick={()=> addText(norm_val)}> 

  let norm_val = 'react';


  function incCounter(){
    setCounter(counter + 1);
  }

  function addText(val){
    setAString(aString + val);
  }


  return (
    <div>

    {button}

      <button onClick={incCounter}> {/*NO (), Important, only runs when clicked*/}
        inc Counter
      </button>

      
      <button onClick={()=> addText(norm_val)}> {/* passing parameters */}
        add text
      }
      </button>
      


    </div>

  )

}
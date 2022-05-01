import React, {useState, createContext, useContext} from 'react';
//import { createContext } from 'react/cjs/react.production.min';

const Context = createContext(); // set up

export function TokenContextProvider({children}) {

    const [token, setToken] = useState(null);
    const [dummy, setDummy] = useState(null);
  
    //console.log(backendurl);
    return (
        <Context.Provider value={{token, setToken, dummy, setDummy}}>
            {children}
        </Context.Provider>
    )
}

export function useTokenContext(){
    return(
        useContext(Context)
    )
}
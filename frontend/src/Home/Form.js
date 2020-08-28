import React, { useState } from 'react';
import Books from './Books';
import './Home.css'

function Form() {
    const [ user, setUser ] = useState('')
    const [ username, setUsername ] = useState('')

    const getRecommendation = async (e) => {
        e.preventDefault()
        if(user)
            setUsername(user)
    }


    return (
        <div>
            <form onSubmit={getRecommendation}>
                <label>
                    Username:<br/>
                    <input type="text" value={user} onChange={e => setUser(e.target.value)} /><br/>
                </label>
                
                <input type="submit" value="Submit"/>
            </form>

            <Books username={username}/>
        </div>
    )
}

export default Form;
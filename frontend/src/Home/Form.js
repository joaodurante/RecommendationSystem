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
        <div className="user-form">
            <form onSubmit={getRecommendation}>
                <label>
                    <input type="text" value={user} onChange={e => setUser(e.target.value)} placeholder="Username"/><br/>
                </label>
                
                <button type="submit">Submit</button>
            </form>

            <Books username={username}/>
        </div>
    )
}

export default Form;
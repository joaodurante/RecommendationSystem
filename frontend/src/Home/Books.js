import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Home.css'

function Books(props) {
    const [ recommendations, setRecommendations ] = useState([])

    useEffect(()=>{
        const getRecommendations = async () => {
            const res = await axios.get(`http://localhost:8000/${props.username}`)
            setRecommendations(res.data)
        }
        
        getRecommendations()
    }, [props.username]);


    return (
        <div>
            {recommendations.length > 0 ? (
                <ul>
                    {recommendations.map(item => <li key={item.name}>{item.name} - {item.totalWeight}</li>)}
                </ul>
            ) : console.log('empty')}
        </div>
    )
}

export default Books;
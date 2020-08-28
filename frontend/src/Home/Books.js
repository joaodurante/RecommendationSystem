import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Home.css'

function Books(props) {
    const [ recommendations, setRecommendations ] = useState([])

    useEffect(()=>{
        const getRecommendations = async () => {
            const res = await axios.get(`http://localhost:8000/${props.username}`)
            setRecommendations(res.data)
            console.log(res.data)
        }
        getRecommendations()
        
    }, [props.username]);


    return (
        <div>
            {recommendations.length > 0 ? (
                <ul>
                    {recommendations.map(item => 
                        <li key={item.name}>
                            <img src={item.imgUrl} alt={item.name} />
                            <p>{item.name}</p>
                            <p>{item.totalWeight}</p>
                        </li>
                    )}
                </ul>
            ) : console.log('empty')}
        </div>
    )
}

export default Books;
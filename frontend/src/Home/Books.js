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
        <div className="books-list">
            {recommendations.length > 0 ? (
                <div>
                    <h3 className="books-title">Livros recomendados</h3>
                    <ul>
                        {recommendations.map(item => 
                            <li key={item.name}>
                                <img src={item.imgUrl} alt={item.name} />
                                <p>{item.name}</p>
                                <p>Weight: {item.totalWeight}</p>
                            </li>
                        )}
                    </ul>
                </div>
            ) : (
                <div className="empty">
                    <h3>Não temos nenhuma recomendação por enquanto</h3>
                </div>
            )}
        </div>
    )
}

export default Books;
import React from 'react';
import { NavLink } from 'react-router-dom';
import './SmallAnimalTile.css';


function SmallAnimalTile({ animal }) {
    return (
        <div className='animal-tile' key={`${animal.id}`}>
            <NavLink to={`/animals/${animal.id}`}>
                <img src={animal.photos[0]?.image_url} alt={"👽"} className='animal-img'/>
                <div>{`${animal.name}`}</div>
            </NavLink>
        </div>
    )
}

export default SmallAnimalTile;

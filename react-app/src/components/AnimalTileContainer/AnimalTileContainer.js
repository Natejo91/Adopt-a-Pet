import React from 'react';
import { useSelector } from 'react-redux';
import SmallAnimalTile from '../SmallAnimalTile/SmallAnimalTile';
import './AnimalTileContainer.css';


function AnimalTileContainer({ loaded }) {
    console.log(loaded, '---------------')
    const state = useSelector(state => state.animals)
    const animals = state.animals


    return (
        <div className='animal-tile-container'>
            <div className='animal-list'>
                {animals.slice(5, 15).map((animal, i) => (
                    <SmallAnimalTile animal={animal} key={i} />
                ))}
            </div>
        </div>
    )






}

export default AnimalTileContainer;

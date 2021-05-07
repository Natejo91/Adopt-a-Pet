import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { getBreed } from '../../store/breeds';
import './AnimalDescription.css';


function AnimalDescription({ animal, shelter }) {
    const dispatch = useDispatch();
    const location = shelter.address
    const array = location.split(' ')
    const newArray = array.slice(0, 2)
    const cityState = newArray.join(' ')

    useEffect(() => {
        dispatch(getBreed(animal.breed_id))
    }, [dispatch])

    return (
        <div className="animal-container">
            <h1>{animal.name}</h1>
            <div>
                {cityState}
            </div>
            <div className="type-age-gender">
                {animal.age} | {animal.gender} | {animal.type}
            </div>
            <div className="animal-description">
                {animal.description}
            </div>
        </div>
    )
}


export default AnimalDescription;

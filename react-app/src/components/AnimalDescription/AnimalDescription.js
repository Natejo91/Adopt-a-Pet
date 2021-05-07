import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getBreed } from '../../store/breeds';

import './AnimalDescription.css';


function AnimalDescription({ animal, shelter }) {
    const dispatch = useDispatch();
    const location = shelter.address
    const array = location.split(' ')
    const newArray = array.slice(0, 2)
    const cityState = newArray.join(', ')
    const breed = useSelector(state => state.breeds?.breed)

    useEffect(() => {
        dispatch(getBreed(animal.breed_id))
    }, [dispatch])

    if (!breed) return null

    return (
        <>
            {breed.name && (
                <div className="animal-container">
                    <h1>{animal.name}</h1>
                    <div>
                        {breed.name} | {cityState}
                    </div>
                    <div className="border-line"></div>
                    <div className="type-age-gender">
                        {animal.age} | {animal.gender} | {animal.type}
                    </div>
                    <div className="border-line"></div>
                    <div className="animal-description">
                        <h1>Meet {animal.name}</h1>
                        {animal.description}
                    </div>
                </div>
            )}
        </>
    )
}


export default AnimalDescription;

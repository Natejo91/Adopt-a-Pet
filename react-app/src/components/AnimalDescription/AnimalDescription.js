import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getBreed } from '../../store/breeds';

import './AnimalDescription.css';


function AnimalDescription({ animal, shelter }) {
    const dispatch = useDispatch();
    const breed = useSelector(state => state.breeds?.breed)

    useEffect(() => {
        dispatch(getBreed(animal.breed_id))
    }, [dispatch, animal.breed_id])

    if (!breed) return null

    return (
        <>
            {breed.name && (
                <div className="animal-container">
                    <h1>{animal.name}</h1>
                    <div>
                        {breed.name}
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
            {breed.name && (
                <div className="breed-container">
                    <div className="breed-image-container">
                        <img src={breed.image_url} alt={"👽"} className="breed-img"/>
                    </div>
                    <div className="breed-name">
                        <h1>{breed.name}</h1>
                    </div>
                    <div className="breed-description">
                        Traits you can find in the  the {breed.name} include <br></br> <strong>{breed.description}</strong>.
                    </div>

                </div>
            )}
        </>
    )
}


export default AnimalDescription;

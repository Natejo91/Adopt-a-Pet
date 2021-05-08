import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneAnimal } from '../../store/animals';
import AnimalDescription from '../AnimalDescription/AnimalDescription';
import ShelterDescription from '../ShelterDescription/ShelterDescription';

import './AnimalPage.css';


function AnimalPage() {
    const dispatch = useDispatch();
    const { id } = useParams();

    const animalId = id

    useEffect(() => {
        dispatch(getOneAnimal(animalId))
    }, [dispatch, animalId])

    const animal = useSelector(state => state.animals.animal)
    const shelter = useSelector(state => state.animals.shelter)

    if (!animal) return null
    if (!shelter) return null

    if (animal[0].photos[1]) {
        var sessionLink = <img className="animal-image" src={animal[0].photos[1]['image_url']}/>
    } else {
        var sessionLink = <div></div>
    }

    if (animal[0].photos[2]) {
        var sessionLink2 = <img className="animal-image" src={animal[0].photos[2]['image_url']}/>
    } else {
        var sessionLink2 = <div></div>
    }

    //need to implement carousel here for animals with multiple photos
    return (
        <>
            <div className="animal-image-container">
                <img className="animal-image" src={animal[0].photos[0]['image_url']} />
                {sessionLink}
                {sessionLink2}
            </div>
            <ShelterDescription shelter={shelter[0]}/>
            <AnimalDescription animal={animal[0]} shelter={shelter[0]}/>
        </>
    )
}


export default AnimalPage;

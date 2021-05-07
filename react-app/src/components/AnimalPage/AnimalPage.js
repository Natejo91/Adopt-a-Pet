import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneAnimal } from '../../store/animals';
import AnimalDescription from '../AnimalDescription/AnimalDescription';

import './AnimalPage.css';


function AnimalPage() {
    const dispatch = useDispatch();
    const { id } = useParams();

    const animalId = id

    useEffect(() => {
        dispatch(getOneAnimal(animalId))
    }, [dispatch])

    const animal = useSelector(state => state.animals.animal)
    const shelter = useSelector(state => state.animals.shelter)

    if (!animal) return null


    return (
        <>
            <h1>Inside Animal Component</h1>
            <AnimalDescription animal={animal[0]} shelter={shelter[0]}/>
        </>
    )
}


export default AnimalPage;

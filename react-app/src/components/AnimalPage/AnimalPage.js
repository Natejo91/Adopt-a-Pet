import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneAnimal } from '../../store/animals';
import './AnimalPage.css';


function AnimalPage() {
    const dispatch = useDispatch();
    const { id } = useParams;
    const animalId = parseInt(id)

    let animal = useSelector(state => state.animals)

    useEffect(() => {
        dispatch(getOneAnimal(animalId))
    }, [dispatch])


    return (
        <>
            {animal.name}
        </>
    )
}


export default AnimalPage;

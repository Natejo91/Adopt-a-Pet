import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneAnimal } from '../../store/animals';
import { getOneShelter } from '../../store/shelters';
import './AnimalPage.css';


function AnimalPage() {
    const dispatch = useDispatch();
    const { id } = useParams();

    const animalId = id
    console.log(animalId)
    useEffect(() => {
        dispatch(getOneAnimal(animalId))
    }, [dispatch])

    const animal = useSelector(state => state.animals.animal)

    if (!animal) return null

    console.log(animal)

    const shelterId = animal['shelter_id']
    console.log(shelterId)

    // useEffect(() => {
    //     dispatch(getOneShelter(shelterId))
    // }, [dispatch])



    return (
        <>
            <h1>Inside Animal Component</h1>
            {/* {animal.name} */}
        </>
    )
}


export default AnimalPage;

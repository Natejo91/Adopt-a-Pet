import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import SmallAnimalTile from '../SmallAnimalTile/SmallAnimalTile';
import { getOneShelter } from '../../store/shelters';
import './ShelterPage.css';



function ShelterPage() {
    const dispatch = useDispatch();
    const { id } = useParams();
    const shelterId = id

    useEffect(() => {
        dispatch(getOneShelter(shelterId))
    }, [dispatch])

    const sheltersAnimals = useSelector(state => state.shelters?.shelters)
    if (!sheltersAnimals) return null;

    const animals = sheltersAnimals[0].animals

    return (
        <div className="shelter-animal-list">
            {animals.map((animal, i) => (
                <SmallAnimalTile animal={animal} key={i} />
            ))}
        </div>
    )
}


export default ShelterPage;

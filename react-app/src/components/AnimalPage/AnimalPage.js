import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneAnimal } from '../../store/animals';
import AnimalDescription from '../AnimalDescription/AnimalDescription';
import ShelterDescription from '../ShelterDescription/ShelterDescription';
import AdoptionForm from '../AdoptionForm/AdoptionForm';
import './AnimalPage.css';


function AnimalPage() {
    const dispatch = useDispatch();
    const { id } = useParams();

    const animalId = id

    useEffect(() => {
        dispatch(getOneAnimal(animalId))
    }, [dispatch, animalId])

    const user = useSelector(state => state.session.user)
    const animal = useSelector(state => state.animals.animal)
    const shelter = useSelector(state => state.animals.shelter)

    if (!animal) return null
    if (!shelter) return null

    let sessionLink;
    if (animal[0].photos[1]) {
        sessionLink = <img className="animal-image" src={animal[0].photos[1]['image_url']} alt={"👽"}/>
    } else {
        sessionLink = <div></div>
    }

    let sessionLink2;
    if (animal[0].photos[2]) {
        sessionLink2 = <img className="animal-image" src={animal[0].photos[2]['image_url']} alt={"👽"}/>
    } else {
        sessionLink2 = <div></div>
    }

    //need to implement carousel here for animals with multiple photos
    return (
        <>
            <div className="animal-image-container">
                <img className="animal-image" src={animal[0].photos[0]['image_url']} alt={"👽"}/>
                {sessionLink}
                {sessionLink2}
            </div>
            <ShelterDescription shelter={shelter[0]}/>
            <AnimalDescription animal={animal[0]} shelter={shelter[0]}/>
            {user &&
                <div className="adoption-container">
                    <h1>Ask about {animal[0].name}!</h1>
                    <div className="user-info">
                        <p><strong>From</strong> <br/>
                            {user.first_name} {user.last_name} <br/>
                            {user.email}
                        </p>
                    </div>
                    <AdoptionForm animal={animal} />
                </div>
            }
        </>
    )
}


export default AnimalPage;

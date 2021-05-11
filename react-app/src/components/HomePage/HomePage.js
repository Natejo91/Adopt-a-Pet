import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAnimals } from '../../store/animals';
import { getShelters } from '../../store/shelters';
import { removeBreeds } from '../../store/breeds';
import { getUserFavorites } from '../../store/favorites';
import AnimalTileContainer from '../AnimalTileContainer/AnimalTileContainer';
import AdoptAPet from '../../public/images/Adopt-A-Pet.png'
import './HomePage.css';



function HomePage(){
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const animals = useSelector(state => state.animals?.animals);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        if (user) {
            const userId = user.id
            dispatch(getAnimals())
            dispatch(getShelters())
            dispatch(removeBreeds())
            dispatch(getUserFavorites(userId))
            setLoaded(true)
        } else {
            dispatch(getAnimals())
            dispatch(getShelters())
            dispatch(removeBreeds())
            setLoaded(true)
        }
    }, [dispatch, user])


    if (!animals) return null


    if (!loaded) return null
    return (
        <>
            <div>
                <img src={AdoptAPet} id='banner' alt={"👽"}/>
            </div>
            <div className='animals-container'>
                <AnimalTileContainer />
            </div>
        </>
    )
}


export default HomePage;

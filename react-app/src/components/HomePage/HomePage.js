import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAnimals } from '../../store/animals';
import AnimalTileContainer from '../AnimalTileContainer/AnimalTileContainer';
import './HomePage.css';



function HomePage(){
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        if (user) {
            dispatch(getAnimals())
        } else {
            dispatch(getAnimals())
        }
    }, [dispatch, user])

    const animals = useSelector(state => state.animals)

    if (!animals) return null



    return (
        <>
            <div className="banner">

            </div>
            <div className='animals-container'>
                <AnimalTileContainer />
            </div>
        </>
    )
}


export default HomePage;

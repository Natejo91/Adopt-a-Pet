import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { addUserFavorite, removeUserFavorite } from '../../store/favorites';
import { faHeart } from '@fortawesome/free-solid-svg-icons';
import { faHeart as farHeart } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import './SmallAnimalTile.css';




function SmallAnimalTile({ animal }) {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session?.user)
    const [loaded, setLoaded] = useState(false);
    const handleClick = async (animalId) => {
        if (!user.favorite_animals[animal.id]) {
            await dispatch(addUserFavorite(animalId, user.id))
            setLoaded(true)
        } else {
            await dispatch(removeUserFavorite(animalId, user.id))
            setLoaded(false)
        }
    }
    useEffect(() => {
        if (user && user.favorite_animals[animal.id]) {
            setLoaded(true)
        } else if (user && !user.favorite_animals[animal.id]) {
            setLoaded(false)
        }
    }, [user?.favorite_animals[animal.id], user, animal.id])

    return (
        <>
            <div className='animal-tile' key={`${animal.id}`}>
                <NavLink to={`/animals/${animal.id}`}>
                    <img src={animal.photos[0]?.image_url} alt={"👽"} className='animal-img'/>
                    <div className='animal-name'>{`${animal.name}`}</div>
                </NavLink>
                {user && loaded &&
                    <div className="heart-filled" onClick={() => handleClick(animal.id)}>
                        <FontAwesomeIcon icon={faHeart} size="2x" color="green"/>
                    </div>
                }
                {user && !loaded &&
                    <div className="heart-button" onClick={() => handleClick(animal.id)}>
                        <FontAwesomeIcon icon={farHeart} size="2x" color="green"/>
                    </div>
                }
            </div>
        </>

    )

}

export default SmallAnimalTile;

import React, { useEffect, useState } from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { addUserFavorite, removeUserFavorite } from '../../store/favorites';
import { faHeart, faTrash } from '@fortawesome/free-solid-svg-icons';
import { faHeart as farHeart } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import './SmallAnimalTile.css';




function SmallAnimalTile({ animal }) {
    const history = useHistory();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session?.user)
    const [loaded, setLoaded] = useState(false);
    const handleClick = (animalId) => {

        if (!user?.favorite_animals[animal.id]) {
            dispatch(addUserFavorite(animalId, user.id))
            setLoaded(true)
        } else {
            dispatch(removeUserFavorite(animalId, user.id))
            setLoaded(false)
        }
    }

    let sessionLinks;
    if (user) {
        sessionLinks = (
            <>
                <div onClick={(() => {handleClick(animal.id)})} className="favorite-button">
                    <FontAwesomeIcon icon={farHeart} />
                </div>
            </>
        )
    }

    return (
        <div className='animal-tile' key={`${animal.id}`}>
            <NavLink to={`/animals/${animal.id}`}>
                <img src={animal.photos[0]?.image_url} alt={"👽"} className='animal-img'/>
                <div className='animal-name'>{`${animal.name}`}</div>
            </NavLink>
            {sessionLinks}
            {user?.favorite_animals[animal.id] &&
                <div>
                    <FontAwesomeIcon icon={faHeart} />
                </div>
            }
        </div>
    )
}

export default SmallAnimalTile;

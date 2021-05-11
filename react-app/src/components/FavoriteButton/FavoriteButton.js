import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { addUserFavorite, removeUserFavorite } from '../../store/favorites';

function FavoriteButton({ animal, favorites}) {
    const history = useHistory();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session?.user)
    const [loaded, setLoaded] = useState(false);

    const handleClick = (animalId) => {
        if (user && !loaded) {
            dispatch(addUserFavorite(animalId, user.id))
            setLoaded(true)
            console.log(loaded)
        } else if (user && loaded){
            dispatch(removeUserFavorite(animalId, user.id))
        }
    }

    return (
        <div onClick={(() => {handleClick(animal.id)})} className="favorite-button">
            HELOO
        </div>
    )
}


export default FavoriteButton;

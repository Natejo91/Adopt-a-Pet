import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import SmallAnimalTile from '../SmallAnimalTile/SmallAnimalTile';
import { getUserFavorites } from '../../store/favorites';


function FavoritesPage() {
    const dispatch = useDispatch();
    const favorites = useSelector(state => state.favorites?.favorites)

    // useEffect(() => {
    //     dispatch(getUserFavorites())
    // }, [dispatch])

    return (
        <>
            <div>
                <h1>Your Favorite Animals!</h1>
            </div>
            <div className='favorite-tile-container'>
                <div className='favorite-list'>
                    {favorites?.map((favorite, i ) => (
                        <SmallAnimalTile animal={favorite} key={i}/>
                    ))}
                </div>

            </div>
        </>
    )
}

export default FavoritesPage;

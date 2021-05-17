import React from 'react';
import { useSelector } from 'react-redux';
import SmallAnimalTile from '../SmallAnimalTile/SmallAnimalTile';
import './SearchResultPage.css';

function SearchResultPage() {

    const type_results = useSelector(state => state.search?.animals_by_type)
    const breed_results = useSelector(state => state.search?.animals_by_breed)

    return (
        <div className="search-results-container">
            <div className="search-page-header">
                <h1>Your search results</h1>
            </div>
            {type_results.map((animal, i) => (
                    <SmallAnimalTile animal={animal} key={i} />
                ))}
            {breed_results.map((animal, i) => (
                    <SmallAnimalTile animal={animal} key={i}/>
                ))}
        </div>
    )
}

export default SearchResultPage;

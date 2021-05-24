import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { getSearch } from '../../store/search';
import './Search.css';

function Search() {
    const dispatch = useDispatch();
    const history = useHistory();
    const [search, setSearch] = useState('');


    const handleSearch = async (e) => {
        e.preventDefault();
        await dispatch(getSearch(search))
        history.push(`/search`)
    }

    return (
        <div>
            <form method="get" action={`/api/search/`} onSubmit={(e) => handleSearch(e)}>
                <input
                    value={search}
                    placeholder='        Dog | Cat | Breed'
                    onChange={(e) => setSearch(e.target.value)}
                    className="search-input"
                />
                <div>
                    <button className="search-btn" onClick={(e) => handleSearch(e)} type="submit">Search</button>
                </div>
            </form>
        </div>
    )

}

export default Search;

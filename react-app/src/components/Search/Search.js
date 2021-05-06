import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { getSearch } from '../../store/search';
import './Search.css';

function Search() {
    const dispatch = useDispatch();
    // const history = useHistory();
    const [search, setSearch] = useState('');


    const handleSearch = async (e) => {
        e.preventDefault();
        await dispatch(getSearch(search))
        // history.push('/search')
    }

    return (
        <div>
            <form method="get" action="/api/search" onSubmit={(e) => handleSearch(e)}>
                <input
                    value={search}
                    placeholder='Search...'
                    onChange={(e) => setSearch(e.target.value)}
                />
                <button onClick={(e) => handleSearch(e)} type="submit">
                    Search
                </button>
            </form>
        </div>
    )

}

export default Search;

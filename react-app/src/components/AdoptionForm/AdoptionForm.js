import React from 'react';
import { useSelector } from 'react-redux';
import './AdoptionForm.css';


const AdoptionForm = () => {
    const user = useSelector(state => state.session?.user);
    const [name, setName] = useState('');


    return (
        <>
        </>
    )
}

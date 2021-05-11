import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addAdoption } from '../../store/adoptions';
import './AdoptionForm.css';


const AdoptionForm = ({ animal }) => {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session?.user);
    const [message, setMessage] = useState('');
    const [errors, setErrors] = useState([]);

    const onSubmit = (e) => {
        e.preventDefault();
        const data = dispatch(addAdoption(user.id, animal[0].id, message))
        if (data.errors) {
            setErrors(data.errors);
        }
        alert('Your message has been sent!')
    }

    const updateMessage = (e) => {
        setMessage(e.target.value);
    }

    return (
        <>
            <form onSubmit={onSubmit}>
                <div>
                    {errors.map((error) => (
                        <div>{error}</div>
                    ))}
                </div>
                <div>
                    <textarea
                        id="text-area"
                        type="text"
                        name="message"
                        onChange={updateMessage}
                        value={message}
                        placeholder={`I'm wondering if ${animal[0].name} is...`}
                    />
                </div>
                <div>
                    <button type="submit">Send Message</button>
                </div>
            </form>
        </>
    )
}


export default AdoptionForm;

import React, { useState } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { updateUser } from '../../store/session';
import { hideUploadModal } from '../../store/modals';
import './UpdateUserForm.css';

function UpdateUserForm() {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user)
    const userImage = useSelector(state => state.session.user.image_url)
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const [image, setImage] = useState(userImage)
    const [errors, setErrors] = useState([]);
    const [zipcode, setZipcode] = useState(11111);
    const [password, setPassword] = useState('');
    const [repeatPassword, setRepeatPassword] = useState('');


    if (!user) return null;


    const update = async (e) => {
        e.preventDefault();
        if (password === repeatPassword) {
            const data = await dispatch(updateUser(firstname, lastname, zipcode, password, image));
            if (data.errors) {
                setErrors(data.errors);
            } else {
                dispatch(hideUploadModal())
            }
        } else {
            setErrors(['Passwords do not match'])
        }
    };


    const updateFirstname = (e) => {
        setFirstname(e.target.value);
    };

    const updateLastname = (e) => {
        setLastname(e.target.value);
    }

    const updateZipcode = (e) => {
        setZipcode(e.target.value)
    }

    const updatePassword = (e) => {
        setPassword(e.target.value);
    }

    const updateRepeatPassword = (e) => {
        setRepeatPassword(e.target.value)
    }

    const updateImage = (e) => {
        const file = e.target.files[0];
        setImage(file)
    }


    return (
        <>
            <form onSubmit={update}>
                <div className="errors-container">
                    {errors.map((error, i) => (
                        <div className="errors" key={i}>{error}</div>
                    ))}
                </div>
                <div className="firstname-container">
                    <label className="firstname-label">First Name</label>
                    <input
                        className="firstname-input"
                        type="text"
                        name="first_name"
                        onChange={updateFirstname}
                        placeholder={user.first_name}
                        required
                    >
                    </input>
                </div>
                <div className="lastname-container">
                    <label className="lastname-label">Last Name</label>
                    <input
                        className="lastname-input"
                        type="text"
                        name="last_name"
                        onChange={updateLastname}
                        placeholder={user.last_name}
                        required
                    >
                    </input>
                </div>
                <div className="zipcode-container">
                    <label className="zipcode-label">Zipcode</label>
                    <input
                        className="zipcode-input"
                        type="number"
                        name="zipcode"
                        onChange={updateZipcode}
                        placeholder={user.zipcode}
                        required
                    >
                    </input>
                </div>
                <div className="password-container">
                    <label className="password-label">Password</label>
                    <input
                        className="password-input"
                        type="password"
                        name="password"
                        onChange={updatePassword}
                        value={password}
                        required
                    >
                    </input>
                </div>
                <div className="confirm-container">
                    <label className="confirm-label">Confirm<br/><span className="span-password">Password</span></label>
                    <input
                        className="confirm-input"
                        type="password"
                        name="repeat_password"
                        onChange={updateRepeatPassword}
                        value={repeatPassword}
                        required
                    >
                    </input>
                </div>
                <div className="photo-container">
                    <label className="photo-label">Photo Url</label>
                    <input
                        className="photo-input"
                        type="file"
                        accept="image/*"
                        onChange={updateImage}
                    ></input>
                </div>
                <div>
                    <button className="update-btn" type="submit">Update</button>
                </div>
            </form>
        </>
    )
}


export default UpdateUserForm;

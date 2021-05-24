import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from 'react-router-dom';
import { signUp } from '../../../store/session';
import './SignUpForm.css';

const SignUpForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session?.user);
  const [image, setImage] = useState(null);
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [errors, setErrors]  = useState([]);
  const [zipcode, setZipcode] = useState(11111);
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  const background = document.querySelector('#modal-background')

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(firstname, lastname, email, image, zipcode, password));
      if (data.errors) {
        setErrors(data.errors);
      } else {
        background.click();
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
  };

  const updateEmail= (e) => {
    setEmail(e.target.value);
  };

  const updateZipcode = (e) => {
    setZipcode(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  }

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  }

  const updateImage = (e) => {
    const file = e.target.files[0];
    setImage(file)
  }

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="signup-container">
      <h1 className="singup">Sign Up</h1>
      <form onSubmit={onSignUp}>
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
            value={firstname}
            required={true}
          ></input>
        </div>
        <div className="lastname-container">
          <label className="lastname-label">Last Name</label>
          <input
            className="lastname-input"
            type="text"
            name="last_name"
            onChange={updateLastname}
            value={lastname}
            required={true}
          ></input>
        </div>
        <div className="email-container">
          <label className="email-label">Email</label>
          <input
            className="email-input"
            type="email"
            name="email"
            onChange={updateEmail}
            value={email}
            required={true}
          ></input>
        </div>
        <div className="zipcode-container">
          <label className="zipcode-label">Zipcode</label>
          <input
            className="zipcode-input"
            type="number"
            name="zipcode"
            onChange={updateZipcode}
            value={zipcode}
            required={true}
          ></input>
        </div>
        <div className="password-container">
          <label className="password-label">Password</label>
          <input
            className="password-input"
            type="password"
            name="password"
            onChange={updatePassword}
            value={password}
            required={true}
          ></input>
        </div>
        <div className="confirm-container">
          <label className="confirm-label">Confirm<br/><span className="span-password">Password</span></label>
          <input
            className="confirm-input"
            type="password"
            name="repeat_password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
          ></input>
        </div>
        <div className="photo-required">
          <h3>Profile Photo Not Required</h3>
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
          <button className="signup-btn" type="submit">Sign Up</button>
        </div>
      </form>
    </div>
  );
};

export default SignUpForm;

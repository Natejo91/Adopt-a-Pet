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
      const data = dispatch(signUp(firstname, lastname, email, image, zipcode, password));
      if (data.errors) {
        setErrors(data.errors);
      } else {
        background.click();
      }
    };
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
        <div>
          {errors.map((error) => (
            <div>{error}</div>
          ))}
        </div>
        <div>
          <label>First Name</label>
          <input
            type="text"
            name="first_name"
            onChange={updateFirstname}
            value={firstname}
          ></input>
        </div>
        <div>
          <label>Last Name</label>
          <input
            type="text"
            name="last_name"
            onChange={updateLastname}
            value={lastname}
          ></input>
        </div>
        <div>
          <label>Email</label>
          <input
            type="text"
            name="email"
            onChange={updateEmail}
            value={email}
          ></input>
        </div>
        <div>
          <label>Zipcode</label>
          <input
            type="number"
            name="zipcode"
            onChange={updateZipcode}
            value={zipcode}
          ></input>
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            name="password"
            onChange={updatePassword}
            value={password}
          ></input>
        </div>
        <div>
          <label>Confirm Password</label>
          <input
            type="password"
            name="repeat_password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
          ></input>
        </div>
        <div>
          <label>Photo Url</label>
          <input
            type="file"
            accept="image/*"
            onChange={updateImage}
          ></input>
        </div>
        <div className="signup-button">
          <button type="submit">Sign Up</button>
        </div>
      </form>
    </div>
  );
};

export default SignUpForm;

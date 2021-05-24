import React, { useState } from "react";
import  { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../../store/session";
import './LoginForm.css';

const LoginForm = () => {
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector(state => state.session?.user);
  const demoEmail = 'demo@aa.io';
  const demoPassword = 'password';

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors)
    }
  };

  const handleDemoLogin = (e) => {
    e.preventDefault();
    dispatch(login(demoEmail, demoPassword))
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login-container">
      <h1>Log In</h1>
      <form onSubmit={onLogin}>
        <div className="errors-container">
          {errors.map((error, i) => (
            <div className="errors" key={i}>{error}</div>
          ))}
        </div>
        <div className="email-container">
          <label className="email-label" htmlFor="email">Email</label>
          <input
            className="email-input"
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
            required
          />
        </div>
        <div className="password-container">
          <label className="password-label" htmlFor="password">Password</label>
          <input
            className="password-input"
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
            required
          />
        </div>
        <div className="login-button-container">
          <button className="login-btn" type="submit">Login</button>
        </div>
      </form>
      <form onSubmit={handleDemoLogin}>
        <button className="demo-btn" type="submit">Demo User</button>
      </form>
    </div>
  );
};

export default LoginForm;

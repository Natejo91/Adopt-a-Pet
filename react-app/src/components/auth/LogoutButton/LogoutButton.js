import React from "react";
import { useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom';
import { logout } from "../../../store/session";
import './LogoutButton.css';

const LogoutButton = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const onLogout = async () => {
    await dispatch(logout());
    history.push('/')

  };

  return (
    <div className="wrap">
      <button className="button" onClick={onLogout}>Logout</button>
    </div>
    )
};

export default LogoutButton;

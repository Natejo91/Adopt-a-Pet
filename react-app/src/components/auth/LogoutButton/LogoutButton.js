import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../../store/session";
import './LogoutButton.css';

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    await dispatch(logout());
  };

  return (
    <div className="wrap">
      <button className="button" onClick={onLogout}>Logout</button>
    </div>
    )
};

export default LogoutButton;

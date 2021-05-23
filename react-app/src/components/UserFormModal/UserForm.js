import React from "react";
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import UpdateUserFormModal from '../UpdateUserFormModal';
import './UserForm.css';

function UserForm() {
  const user = useSelector(state => state.session.user)


  if (!user) {
    return null;
  }

  return (
    <>
      <div className="profile-container">
        <div className="profile-photo-container">
          <img id="profile-photo" src={user.image_url} alt="User profile picture"/>
        </div>
        <div className="firstname-profile-container">
          <strong>First Name | </strong> {user.first_name}
        </div>
        <div className="lastname-profile-container">
          <strong>Last Name | </strong> {user.last_name}
        </div>
        <div className="email-profile-container">
          <strong>Email | </strong> {user.email}
        </div>
        <div className="zipcode-profile-container">
          <strong>Zipcode | </strong> {user.zipcode}
        </div>
        {/* possibly put users favorite animals names here as well */}
      </div>
      <div className="update-container">
        <UpdateUserFormModal />
      </div>
    </>

  );
}
export default UserForm;

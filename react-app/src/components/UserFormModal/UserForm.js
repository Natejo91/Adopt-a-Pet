import React from "react";
import { useSelector, useDispatch } from 'react-redux';
import { deleteUser, logout} from '../../store/session';
import { useHistory } from 'react-router-dom';
import UpdateUserFormModal from '../UpdateUserFormModal';
import './UserForm.css';

function UserForm() {
  const history = useHistory();
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user)

  const removeUser = async (e) => {
    e.preventDefault();
    await dispatch(deleteUser())
    await dispatch(logout())
    await history.push('/');
}


  if (!user) {
    return null;
  }

  return (
    <>
      <div className="profile-container">
        <div className="profile-photo-container">
          <img id="profile-photo" src={user.image_url} alt="User profile"/>
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
      {user.id !== 1 &&
        <div className="update-container">
          <UpdateUserFormModal />
        </div>
      }
      {user.id !== 1 &&
        <div className="delete-container">
          <button className="delete-btn" onClick={(e) => removeUser(e)}>Delete Account</button>
        </div>
      }
    </>

  );
}
export default UserForm;

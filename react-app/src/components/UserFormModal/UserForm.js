import React from "react";
import { useSelector } from 'react-redux'
import './UserForm.css';

function UserForm() {
  const user = useSelector(state => state.session.user)


  if (!user) {
    return null;
  }

  return (
    <ul>
      <li>
        <strong>User Id</strong> {user.first_name}
      </li>
      <li>
        <strong>Username</strong> {user.last_name}
      </li>
      <li>
        <strong>Email</strong> {user.email}
      </li>
    </ul>
  );
}
export default UserForm;

import React from 'react';
import { NavLink } from 'react-router-dom';
import { Modal } from '../../context/Modal'
import { useSelector, useDispatch } from 'react-redux';
import UpdateUserForm from '../UpdateUserFormModal/UpdateUserForm';
import LogoutButton from '../auth/LogoutButton/LogoutButton';
import LoginFormModal from '../auth/LoginFormModal';
import SignUpFormModal from '../auth/SignUpFormModal';
import UserFormModal from '../UserProfileModal';
import { hideUploadModal } from '../../store/modals';
import Search from '../Search/Search';
import './NavBar.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPaw, faHome } from '@fortawesome/free-solid-svg-icons';

const NavBar = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session?.user)
  const modalState = useSelector(state => state.modals.showUploadModal)

  const handleClose = () => {
    dispatch(hideUploadModal())
  }

  return (
    <nav>
      <div className="navbar-container">
        <div className="home-icon">
          <NavLink to="/" exact={true} activeClassName="active" >
            <FontAwesomeIcon icon={faHome} size="4x" color="white"/>
          </NavLink>
        </div>
        <div className="login-button">
          {!user &&
            <LoginFormModal />
          }
        </div>
        <div className="signup-button">
          {!user &&
            <SignUpFormModal />
          }
        </div>
        <div className="favorite-icon">
          {user &&
            <NavLink to="/favorites" activeClassName="active">
              <FontAwesomeIcon icon={faPaw} size="4x" color="white"/>
            </NavLink>
          }
        </div>
        <div className="profile-button">
          {user &&
            <>
              <UserFormModal />
              {modalState &&
                <Modal onClose={handleClose}>
                  <UpdateUserForm />
                </Modal>
              }
            </>
          }
        </div>
        {user &&
          <div className="logout-button">
            <LogoutButton />
          </div>
        }
        <div className="search-bar">
          <Search />
        </div>
      </div>
    </nav>
  );
}

export default NavBar;

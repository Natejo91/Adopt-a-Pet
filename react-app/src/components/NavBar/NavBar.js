import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton/LogoutButton';
import LoginFormModal from '../auth/LoginFormModal';
import SignUpFormModal from '../auth/SignUpFormModal';
import UserFormModal from '../UserFormModal';
import Search from '../Search/Search';
import './NavBar.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPaw, faHome } from '@fortawesome/free-solid-svg-icons';

const NavBar = () => {
  const user = useSelector(state => state.session?.user)


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
            <UserFormModal />
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

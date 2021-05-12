import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton/LogoutButton';
import LoginFormModal from '../auth/LoginFormModal';
import SignUpFormModal from '../auth/SignUpFormModal';
import Search from '../Search/Search';
import './NavBar.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHome } from '@fortawesome/free-solid-svg-icons';

const NavBar = () => {
  const user = useSelector(state => state.session?.user)



  return (
    <nav>
      <div className="navbar-container">
        <div>
          <NavLink to="/" exact={true} activeClassName="active" >
            <FontAwesomeIcon icon={faHome} size="2x"/>
          </NavLink>
        </div>
        <div>
          {!user &&
            <LoginFormModal />
          }
        </div>
        <div>
          {!user &&
            <SignUpFormModal />
          }
        </div>
        <div>
          {user &&
            <NavLink to="/favorites" activeClassName="active">
              Favorites
            </NavLink>
          }
        </div>
        <div>
          <NavLink to="/users" exact={true} activeClassName="active">
            Users
          </NavLink>
        </div>
        <div>
          <LogoutButton />
        </div>
        <div>
          <Search />
        </div>
      </div>
    </nav>
  );
}

export default NavBar;

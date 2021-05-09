import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginFormModal/LoginForm";
import SignUpForm from "./components/auth/SignUpFormModal/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList/UsersList";
import User from "./components/User/User";
import HomePage from "./components/HomePage/HomePage";
import AnimalPage from "./components/AnimalPage/AnimalPage";
import SearchResultPage from "./components/SearchResultPage/SearchResultPage";
// import { authenticate } from "./services/auth";
import { authenticate } from "./store/session";

function App() {
  // const [authenticated, setAuthenticated] = useState(false);
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <>
      <NavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>
        <Route path="/" exact={true}>
          <HomePage />
        </Route>
        <Route path="/animals/:id" exact={true}>
          <AnimalPage />
        </Route>
        <Route path="/search" exact={true}>
          <SearchResultPage />
        </Route>
      </Switch>
    </>
  );
}

export default App;

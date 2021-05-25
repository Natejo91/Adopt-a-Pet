import React, { useState } from 'react';
import { Modal } from '../../context/Modal'
import { useDispatch, useSelector } from 'react-redux';
import { showProfileModal } from '../../store/modals';
import UserForm from './UserForm';
import './index.css';

function UserFormModal() {
    const dispatch = useDispatch();
    const [showModal, setShowModal] = useState(false);
    const modalState = useSelector(state => state.modals.showProfileModal)

    const handleClick = () => {
        setShowModal(true)
        dispatch(showProfileModal())
    }

    const handleClose = () => {
        setShowModal(false)
    }

    return (
        <>
            <div className="wrap">
                <button className="button" onClick={handleClick}>Profile</button>
            </div>
            {showModal && modalState && (
                <Modal onClose={handleClose}>
                    <UserForm />
                </Modal>
            )}
        </>
    )
}

export default UserFormModal;

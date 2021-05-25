import React, { useState } from 'react';
import { Modal } from '../../context/Modal'
import UpdateUserForm from './UpdateUserForm';
import { useDispatch, useSelector } from 'react-redux';
import { showUploadModal, hideUploadModal, showProfileModal, hideProfileModal } from '../../store/modals';
import './index.css';

function UpdateUserFormModal() {
    const dispatch = useDispatch();
    const [showModal, setShowModal] = useState(false);
    const modalState = useSelector(state => state.modals.showUploadModal)


    const handleClick = () => {
        dispatch(showUploadModal())
        dispatch(hideProfileModal())
    }

    const handleClose = () => {
        // setShowModal(false)
        dispatch(hideUploadModal())
        // dispatch(showProfileModal())
    }

    return (
        <>
            <div className="wrap">
                <button className="update" onClick={handleClick}>Update Info</button>
            </div>
            {/* {modalState && (
                <Modal onClose={handleClose}>
                    <UpdateUserForm />
                </Modal>
            )} */}
        </>
    )
}

export default UpdateUserFormModal;

import React, { useState } from 'react';
import { Modal } from '../../context/Modal'
import UpdateUserForm from './UpdateUserForm';
import './index.css';

function UpdateUserFormModal() {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div className="wrap">
                <button className="button" onClick={() => setShowModal(true)}>Update Info</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <UpdateUserForm />
                </Modal>
            )}
        </>
    )
}

export default UpdateUserFormModal;

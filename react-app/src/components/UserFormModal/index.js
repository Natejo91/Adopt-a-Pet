import React, { useState } from 'react';
import { Modal } from '../../context/Modal'
import UserForm from './UserForm';
import './index.css';

function UserFormModal() {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div className="wrap">
                <button className="button" onClick={() => setShowModal(true)}>Profile</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <UserForm />
                </Modal>
            )}
        </>
    )
}

export default UserFormModal;

import React, { useState } from 'react';
import { Modal } from '../../../context/Modal';
import SignUpForm from './SignUpForm';

function SignUpFormModal() {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div className="wrap">
                <button className="button" onClick={() => setShowModal(true)}>Sign Up</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <SignUpForm />
                </Modal>
            )}
        </>
    )
}

export default SignUpFormModal;

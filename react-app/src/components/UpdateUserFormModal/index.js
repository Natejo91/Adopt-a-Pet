import React from 'react';
import { useDispatch } from 'react-redux';
import { showUploadModal, hideProfileModal } from '../../store/modals';
import './index.css';

function UpdateUserFormModal() {
    const dispatch = useDispatch();


    const handleClick = () => {
        dispatch(showUploadModal())
        dispatch(hideProfileModal())
    }

    return (
        <>
            <div className="wrap">
                <button className="update" onClick={handleClick}>Update Info</button>
            </div>
        </>
    )
}

export default UpdateUserFormModal;

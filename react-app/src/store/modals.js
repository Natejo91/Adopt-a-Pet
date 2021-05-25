const SHOW_UPLOAD_MODAL = 'modals/SHOW_UPLOAD_MODAL';
const HIDE_UPLOAD_MODAL = 'modals/HIDE_UPLOAD_MODAL';
const SHOW_PROFILE_MODAL = 'modals/SHOW_PROFILE_MODAL';
const HIDE_PROFILE_MODAL = 'modals/HIDE_PROFILE_MODAL';

export const showUploadModal = () => ({
    type: SHOW_UPLOAD_MODAL,

})
export const hideUploadModal = () => ({
    type: HIDE_UPLOAD_MODAL,

})

export const showProfileModal = () => ({
    type: SHOW_PROFILE_MODAL,

})
export const hideProfileModal = () => ({
    type: HIDE_PROFILE_MODAL,

})


const initialState = {showUploadModal: false, showProfileModal: false}

export default function modalReducer(state = initialState, action){
    switch(action.type){
        case SHOW_UPLOAD_MODAL:
            return {...state, showUploadModal: true}

        case HIDE_UPLOAD_MODAL:
            return {...state, showUploadModal: false}
        //case SHOW MESSSAGING
        case SHOW_PROFILE_MODAL:
            return {...state, showProfileModal: true}
        //case HIDE MESSAGING
        case HIDE_PROFILE_MODAL:
            return {...state, showProfileModal: false}
        default:
            return state
    }
}

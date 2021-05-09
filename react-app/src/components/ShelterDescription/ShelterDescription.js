import React from 'react';
import mapLocation from '../../public/images/location.png';
import MapContainer from '../MapContainer/MapContainer';
import phoneIcon from '../../public/images/phone.png';
import emailIcon from '../../public/images/email.png';
import './ShelterDescription.css';



function ShelterDescription({ shelter }) {


    if (!shelter) return null;

    return (
        <>
            {shelter.name && (
                <div className="shelter-container">
                    <div className="shelter-img">
                        <img src={shelter.image_url} alt={"👽"} className="shelter-icon"/>
                    </div>
                    <div className="shelter-description">
                        <div>
                            <MapContainer shelter={shelter}/>
                        </div>
                        <img src={mapLocation} className="location-icon" alt={"👽"}/>
                        <div className="shelter-address">

                            {shelter.address}
                        </div>
                        <div className="shelter-email">
                            <img src={emailIcon} className="email-icon" alt={"👽"}/>
                            {shelter.email}
                        </div>
                        <div className="shelter-phone">
                            <img src={phoneIcon} className="phone-icon" alt={"👽"}/>
                            {shelter.phone_number}
                        </div>

                    </div>
                </div>
            )}
        </>
    )

}


export default ShelterDescription;

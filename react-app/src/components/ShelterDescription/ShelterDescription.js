import React from 'react';
import { Link } from 'react-router-dom';
import mapLocation from '../../public/images/location.png';
import './ShelterDescription.css';


function ShelterDescription({ shelter }) {
    const location = shelter.address
    const array = location.split(' ')
    const newArray = array.slice(0, 2)
    const cityState = newArray.join(', ')

    if (!shelter) return null;

    return (
        <>
            {shelter.name && (
                <div className="shelter-container">
                    <div className="shelter-img">
                        <img src={shelter.image_url} alt={"👽"} className="shelter-icon"/>
                    </div>
                    <div className="shelter-description">
                        {cityState}
                        <div>
                            -------GOOGLE MAP COMPONENT HERE---------
                        </div>
                        <img src={mapLocation} className="location-icon" alt={"👽"}/>
                        Location Address
                        <div className="shelter-address">
                            {shelter.address}
                        </div>
                        <div className="shelter-email">
                            {/* <Link className="mailto" to={`mailto:${shelter.email}`}>{shelter.email}</Link> */}
                        </div>
                        <div className="shelter-phone">
                            {shelter.phone_number}
                        </div>

                    </div>
                </div>
            )}
        </>
    )

}


export default ShelterDescription;

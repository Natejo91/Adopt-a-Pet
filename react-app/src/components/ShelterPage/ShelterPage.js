import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneShelter } from '../../store/shelters';
import SmallAnimalTile from '../SmallAnimalTile/SmallAnimalTile';
import emailIcon from '../../public/images/email.png';
import phoneIcon from '../../public/images/phone.png';
import MapContainer from '../MapContainer/MapContainer';
import mapLocation from '../../public/images/location.png';
import './ShelterPage.css';



function ShelterPage() {
    const dispatch = useDispatch();
    const { id } = useParams();
    const shelterId = id

    useEffect(() => {
        dispatch(getOneShelter(shelterId))
    }, [dispatch, shelterId])

    const shelter = useSelector(state => state.shelters?.shelters)
    if (!shelter) return null;

    const shelterInfo = shelter[0];
    console.log(shelterInfo)

    const animals = shelter[0].animals

    return (
        <>
            <div className="shelter-page-container">
                <div className="shelter-img">
                    <img src={shelterInfo.image_url} alt={"👽"} className="shelter-icon"/>
                </div>
                <div className="shelter-page-description">
                    <div>
                        <MapContainer shelter={shelterInfo}/>
                    </div>
                    <img src={mapLocation} className="location-icon" alt={"👽"}/>
                    <div className="shelter-address">
                        {shelterInfo.address}
                    </div>
                    <div className="shelter-email">
                        <img src={emailIcon} className="email-icon" alt={"👽"}/>
                        {shelterInfo.email}
                    </div>
                    <div className="shelter-phone">
                        <img src={phoneIcon} className="phone-icon" alt={"👽"}/>
                        {shelterInfo.phone_number}
                    </div>
                </div>
            </div>
            <div className="shelter-animal-header">
                <h1>Current pets at {shelterInfo.name}</h1>
            </div>
            <div className="shelter-animal-list">
                {animals.map((animal, i) => (
                    <SmallAnimalTile animal={animal} key={i} />
                ))}
            </div>
        </>
    )
}


export default ShelterPage;

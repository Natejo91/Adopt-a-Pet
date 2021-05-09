import React from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';



const MapContainer = ({ shelter }) => {
    const mapStyles = {
        height: "33vh",
        width: "100%",
    };

    const locations = [
        {
            name: "Dumb Friends League",
            location: {
                lat: 39.7765305,
                lng: -104.9034466
            },
        },
        {
            name: "Bloomington Animal Shelter",
            location: {
                lat: 39.1229602,
                lng: -86.5320942
            },
        },
        {
            name: "Lake Erie Labrador Retriever Rescue",
            location: {
                lat: 41.1383878,
                lng: -81.8637474
            },
        },
        {
            name: "Lamar County Humane Assn.",
            location: {
                lat: 33.6793159,
                lng: -95.5518267
            },
        },
        {
            name: "Montgomery City Animal Shelter/Project Precious Paws",
            location: {
                lat: 38.981577,
                lng: -91.4975276
            },
        },
        {
            name: "Whispurring Hope Rescue",
            location: {
                lat: 42.4844866,
                lng: -91.1254699
            },
        },
        {
            name: "FACE Low-Cost Animal Clinic",
            location: {
                lat: 39.785113,
                lng: -86.1327992
            },
        },
        {
            name: "Warrick Humane Society",
            location: {
                lat: 37.983902,
                lng: -87.354287
            },
        },
        {
            name: "Angels Four Paws",
            location: {
                lat: 41.887871,
                lng: -88.0160332
            },
        },
        {
            name: "Second Chance Pet Rescue",
            location: {
                lat: 39.9276572,
                lng: -122.1791556
            },
        },
        {
            name: "Shawano County Humane Society",
            location: {
                lat: 44.7628786,
                lng: -88.5716306
            },
        },
        {
            name: "Pittsburgh Rat Lovers Club",
            location: {
                lat: 40.4416941,
                lng: -79.9900861
            },
        },
        {
            name: "The Progressive Animal Welfare Society (PAWS)",
            location: {
                lat: 39.4456932,
                lng: -84.4165324
            },
        },
        {
            name: "Stray Hearts Animal Shelter",
            location: {
                lat: 36.385583,
                lng: -105.596715
            },
        },
        {
            name: "Sanctuary Animal Rescue",
            location: {
                lat: 33.267985,
                lng: -86.795479
            }
        }
    ]

    const ApiKey = process.env.REACT_APP_GOOGLE_API_KEY;
    console.log(process.env.REACT_APP_GOOGLE_API_KEY);


    const location = locations.filter(location => {
        if (location.name !== shelter.name) {
            return null;
        }
        return location.location
    })

    const defaultCenter = location[0].location

    return (
        <LoadScript googleMapsApiKey={ApiKey}>
            <GoogleMap mapContainerStyle={mapStyles} zoom={13} center={defaultCenter}>
                <Marker key={shelter.name} position={defaultCenter} />
            </GoogleMap>
        </LoadScript>
    )
}


export default MapContainer;

import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';


const FontAwesome = require('react-fontawesome');

function Footer() {
    return (
        <>
            <div className="footer-container">
                <div className="footer-about">
                    <h2>About Adopt-a-Pet</h2>
                    <p>FAQs <br/>
                    Terms of Service <br/>
                    About Adopt-a-Pet <br />
                    Contact Us <br/>
                    </p>
                </div>
                <div className="footer-adoption">
                    <h2>Pet Adoption</h2>
                    <p>Dog Adoption <br/>
                    Cat Adoption <br/>
                    Other Pet Adoption <br/>
                    Shelters & Rescues <br/>
                    </p>
                </div>
                <div className="footer-information">
                    <h2>Pet Care Information</h2>
                    <p>Dog Care <br/>
                    Dog Breeds <br/>
                    Cat Care <br/>
                    Cat Breeds <br/>
                    </p>
                </div>
            </div>
            <div className="copyright">
                <p>@2021 Adopt-a-Pet.com  |  Nathaniel Ortega all rights reserved.</p>
            </div>
            {/* <FontAwesome icon={faHome}/> */}
        </>
    )
}

export default Footer

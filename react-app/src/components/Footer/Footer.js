import React from 'react';
import './Footer.css';

function Footer() {
    return (
        <>
            <div className="footer-container">
                <div className="footer-donation">
                    <h2 className="footer-headers">Animal Donation</h2>
                    <p><a id="footer" href="https://www.humanesociety.org/how-you-can-help" target="_blank" rel="noopener noreferrer">Humane Society</a> <br/>
                    <a id="footer2" href="https://www.americanhumane.org/" target="_blank" rel="noopener noreferrer">American Humane</a> <br/>
                    </p>
                </div>
                <div className="footer-information">
                    <h2 className="footer-headers">Pet Care Information</h2>
                    <p><a id="footer3" href="https://be.chewy.com/pet-parenting-pet-lovers-dog-adoption-checklist-what-you-need-to-know/?gclid=CjwKCAjw47eFBhA9EiwAy8kzNKdhE_XTh8Zof4N52URRODFnFrA5u4LZazYUWOu0XpvpLMv2pH44lBoCbTcQAvD_BwE" target="_blank" rel="noopener noreferrer">Dog Adoption Checklist</a> <br/>
                    <a id="footer4"href="https://be.chewy.com/cat-adoption-checklist/" target="_blank" rel="noopener noreferrer">Cat Adoption Checklist</a> <br/>
                    <a id="footer5"href="https://www.aspca.org/pet-care/dog-care/general-dog-care" target="_blank" rel="noopener noreferrer">General Dog Care</a> <br/>
                    <a id="footer6" href="https://www.aspca.org/pet-care/cat-care/general-cat-care" target="_blank" rel="noopener noreferrer">General Cat Care</a> <br/>
                    </p>
                </div>
            </div>
            <div className="copyright">
            <a id="footer7" href="https://www.linkedin.com/in/nathaniel-ortega-256673206" target="_blank" rel="noopener noreferrer"><i className="fab fa-linkedin fa-3x"></i></a><p className="rights-reserved">@2021 Adopt-a-Pet.com  |  Nathaniel Ortega all rights reserved.</p><a id="footer8" href="https://github.com/Natejo91/Adopt-a-Pet" target="_blank" rel="noopener noreferrer"><i className="fab fa-github-square fa-3x"></i></a>
            </div>
        </>
    )
}

export default Footer

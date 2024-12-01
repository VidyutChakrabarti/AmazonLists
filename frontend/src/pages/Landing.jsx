import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import * as THREE from 'three';
import FOG from 'vanta/dist/vanta.fog.min';
import '../css/landing.css';

const Landing = () => {
    const vantaRef = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        const vantaEffect = FOG({
            el: vantaRef.current,
            THREE,
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.0,
            minWidth: 200.0,
            highlightColor: 0xff00a5,
            midtoneColor: 0xffb400,
            lowlightColor: 0xff0000,
            blurFactor: 0.24,
            speed: 0.9,
        });

        return () => {
            if (vantaEffect) vantaEffect.destroy();
        };
    }, []);

    const handleBoxClick = () => {
        navigate('/ListProduct');
    };

    return (
        <div className="landing-page">
            <div className="top-bar">
                <img src="logo.png" alt="Logo" className="logo" />
                <div className="brand-title">AmazonLists</div>
            </div>
            <div className="content">
                <div ref={vantaRef} className="white-section"></div>
                <div className="black-section">
                    <div className="grid-container">
                        <div className="column">
                            <div className="box box1" onClick={handleBoxClick}>
                                <div className="heading">List your product</div>
                            </div>
                            <div className="box box2" onClick={handleBoxClick}>
                                <div className="heading">List your product</div>
                            </div>
                        </div>
                        <div className="column">
                            <div className="box box3" onClick={handleBoxClick}>
                                <div className="heading">List your product</div>
                            </div>
                            <div className="box box4" onClick={handleBoxClick}>
                                <div className="heading">List your product</div>
                            </div>
                        </div>
                        <div className="column">
                            <div className="box box5" onClick={handleBoxClick}>
                                <div className="heading">List your product</div>
                            </div>
                            <div className="box box6" onClick={handleBoxClick}>
                                <div className="heading">List your product</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Landing;

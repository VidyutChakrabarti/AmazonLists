import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';
import FOG from 'vanta/dist/vanta.fog.min';
import '../css/landing.css';

const Landing = () => {
    const vantaRef = useRef(null);

    useEffect(() => {
        const vantaEffect = FOG({
            el: vantaRef.current,
            THREE, // Three.js instance
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 400.00,
            highlightColor: 0xffb3,
            midtoneColor: 0xfff0,
            lowlightColor: 0xff77,
            baseColor: 0xebfffa,
            speed: 6.00,
        });

        return () => {
            if (vantaEffect) vantaEffect.destroy();
        };
    }, []);

    return (
        <div ref={vantaRef} className="min-h-screen flex flex-col" style={{ fontFamily: 'Times New Roman' }}>
            <div className="flex-grow-[30] flex flex-col items-start justify-center p-8" style={{ zIndex: 1, color: 'black' }}>
                <h1 className="text-7xl font-bold text-black">AmazonLists</h1>
                <p className="text-lg italic text-black mt-2">Convert your social media posts into a custom amazon product with this fully automated platform!</p>
            </div>
            <div className="flex-grow bg-gray-900 flex flex-col items-start justify-center p-8 space-y-4" style={{ zIndex: 1 }}>
                <h2 className="text-2xl font-semibold text-white">Explore our Functionalities:</h2>
                <ul className="text-lg space-y-2 w-full">
                    <li>
                        <a href="/ListProduct" className="block w-full text-center bg-[#00ef9f] hover:bg-[#d2007e] transition duration-300 text-white font-medium py-3 rounded-lg">
                            List Product
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    );
};

export default Landing;

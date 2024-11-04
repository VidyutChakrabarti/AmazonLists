import React from 'react';
import '../css/landing.css';

const Landing = () => {
    return (
        <div className="min-h-screen flex flex-col" style={{ fontFamily: 'Times New Roman' }}>
            <div className="flex-grow-[30] flex flex-col items-start justify-center gradient-background p-8">
                <h1 className="text-7xl font-bold text-white">AmazonLists</h1>
                <p className="text-lg italic text-white mt-2">Convert your social media posts into a custom amazon product with this fully automated platform!</p>
            </div>
            <div className="flex-grow bg-gray-900 flex flex-col items-start justify-center p-8 space-y-4">
                <h2 className="text-2xl font-semibold text-white">Explore our Functionalities:</h2>
                <ul className="text-lg space-y-2 w-full">
                    <li>
                        <a href="/ListProduct" className="block w-full text-center bg-[#8d3cff] hover:bg-[#d2007e] transition duration-300 text-white font-medium py-3 rounded-lg">
                            List Product
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    );
};

export default Landing;

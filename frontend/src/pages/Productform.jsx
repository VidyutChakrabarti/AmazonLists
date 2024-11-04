import React from 'react';
import axios from 'axios';

const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
        profileLink: formData.get('profile-link'),
        postLinks: formData.get('post-links').split('\n'),
        productName: formData.get('product-name'),
        description: formData.get('description'),
    };
    try {
        const response = await axios.post('http://localhost:8501/submit', data, {
            headers: {
                'Content-Type': 'application/json',
            },
        });

        console.log(response.data);
    } catch (error) {
        console.error('Error:', error);
    }
};

const App = () => {
    return (
        <div className="min-h-screen flex bg-gradient-to-br from-gray-800 via-gray-900 to-black">
            <div className="w-4/6 flex items-center justify-center py-12 px-4 lg:px-8">
                <div className="max-w-4xl w-full bg-gray-900 rounded-lg shadow-lg p-10">
                    <div className="text-center mb-8">
                        <h1 className="text-4xl font-bold text-white">Product Listing Form</h1>
                        <p className="mt-2 text-lg text-sky-400">
                            Enter your product details and relevant links below.
                        </p>
                    </div>
                    <form onSubmit={handleSubmit} className="grid grid-cols-1 gap-8">
                        {/* Profile Link */}
                        <div>
                            <label htmlFor="profile-link" className="block text-sm font-medium text-gray-300">
                                Profile Link
                            </label>
                            <input
                                type="url"
                                name="profile-link"
                                id="profile-link"
                                placeholder="https://profile.com/username"
                                className="mt-1 block w-full px-4 py-3 border border-gray-600 bg-gray-800 text-white rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 sm:text-sm"
                            />
                        </div>

                        {/* Post Links */}
                        <div>
                            <label htmlFor="post-links" className="block text-sm font-medium text-gray-300">
                                Post Links (one per line)
                            </label>
                            <textarea
                                name="post-links"
                                id="post-links"
                                rows="2"
                                placeholder="https://post1.com\nhttps://post2.com"
                                className="mt-1 block w-full px-4 py-3 border border-gray-600 bg-gray-800 text-white rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 sm:text-sm"
                            ></textarea>
                        </div>

                        {/* Product Name */}
                        <div>
                            <label htmlFor="product-name" className="block text-sm font-medium text-gray-300">
                                Product Name
                            </label>
                            <input
                                type="text"
                                name="product-name"
                                id="product-name"
                                placeholder="Product name"
                                className="mt-1 block w-full px-4 py-3 border border-gray-600 bg-gray-800 text-white rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 sm:text-sm"
                            />
                        </div>

                        {/* Product Description */}
                        <div>
                            <label htmlFor="description" className="block text-sm font-medium text-gray-300">
                                Product Description
                            </label>
                            <textarea
                                name="description"
                                id="description"
                                rows="2"
                                placeholder="Enter a brief description of the product"
                                className="mt-1 block w-full px-4 py-3 border border-gray-600 bg-gray-800 text-white rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 sm:text-sm"
                            ></textarea>
                        </div>

                        {/* Submit Button */}
                        <div>
                            <button
                                type="submit"
                                className="w-full py-3 px-6 border border-transparent rounded-md shadow-sm text-lg font-medium text-white bg-gradient-to-r from-sky-500 to-purple-500 hover:from-purple-500 hover:to-sky-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500"
                            >
                                Submit
                            </button>
                        </div>
                    </form>
                </div>
            </div>
            <div className="w-2/6 flex flex-col items-center justify-center p-4 border-l border-gray-700 gradient-background">
                {/* YouTube Video 1 */}
                <div className="mb-8 w-full p-4 bg-gray-800 rounded-lg shadow-md">
                    <iframe
                        width="100%"
                        height="200"
                        src="https://www.youtube.com/embed/VIDEO_ID_1?autoplay=1&loop=1&playlist=VIDEO_ID_1"
                        title="YouTube Video 1"
                        frameBorder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                    ></iframe>
                    <p className="mt-2 text-sm text-gray-300">
                        Description for Video 1: This video showcases the features of our product.
                    </p>
                </div>
                {/* YouTube Video 2 */}
                <div className="w-full p-3 bg-gray-800 rounded-lg shadow-md">
                    <iframe
                        width="100%"
                        height="200"
                        src="https://www.youtube.com/embed/VIDEO_ID_2?autoplay=1&loop=1&playlist=VIDEO_ID_2"
                        title="YouTube Video 2"
                        frameBorder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                    ></iframe>
                    <p className="mt-2 text-sm text-gray-300">
                        Description for Video 2: Here, we dive into the details of how to use the product effectively.
                    </p>
                </div>
            </div>

        </div>
    );
};

export default App;

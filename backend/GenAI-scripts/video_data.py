from models.video import Video

# Video Database by Category
VIDEO_DATABASE = {
    "electronics": {
        "video_123": {
            "title": "iPhone 15 Pro Review",
            "category": "Smartphones",
            "duration": "10:25",
            "highlights": [
                "Camera system demo",
                "Performance benchmarks",
                "Battery life test",
                "Design overview"
            ],
            "transcript_summary": "Detailed review of iPhone 15 Pro features...",
            "key_features": [
                "A17 Pro chip",
                "48MP camera",
                "Titanium design",
                "USB-C port"
            ],
            "price_range": "$999 - $1199"
        },
        "video_124": {
            "title": "MacBook Pro M3 Analysis",
            "category": "Laptops",
            "duration": "15:30",
            "highlights": [
                "Performance tests",
                "Display quality",
                "Battery duration",
                "Port selection"
            ],
            "transcript_summary": "In-depth analysis of the new MacBook Pro...",
            "key_features": [
                "M3 chip",
                "Mini-LED display",
                "Up to 22hr battery",
                "Multiple ports"
            ],
            "price_range": "$1599 - $2499"
        }
    },
    "fashion": {
        "video_125": {
            "title": "Nike Air Jordan Collection",
            "category": "Sneakers",
            "duration": "8:45",
            "highlights": [
                "Design showcase",
                "Comfort testing",
                "Style combinations",
                "Size guide"
            ],
            "transcript_summary": "Comprehensive review of Air Jordan lineup...",
            "key_features": [
                "Air cushioning",
                "Premium materials",
                "Iconic design",
                "Multiple colorways"
            ],
            "price_range": "$180 - $200"
        }
    },
    # Add other categories...
    "beauty": {
        "video_126": {
            "title": "Summer Makeup Tutorial",
            "category": "Makeup",
            "duration": "12:15",
            "highlights": [
                "Product application",
                "Techniques demo",
                "Wear test",
                "Product reviews"
            ],
            "transcript_summary": "Step-by-step summer makeup guide...",
            "key_features": [
                "Waterproof products",
                "Natural look",
                "Long-lasting",
                "SPF protection"
            ],
            "price_range": "$20 - $150"
        }
    }
}

# Sample Videos
sample_videos = [
    # Electronics - Smartphones
    Video(
        title="Samsung Galaxy S24 Ultra Features",
        category="Electronics",
        subcategory="Smartphones",
        duration="11:40",
        views="1.2M",
        highlights=[
            "Camera zoom comparison",
            "Gaming performance test",
            "Battery endurance",
            "New design elements"
        ],
        transcript_summary="Overview of the features and improvements in Samsung Galaxy S24 Ultra...",
        key_features=[
            "200MP camera",
            "Snapdragon 8 Gen 3",
            "5000mAh battery",
            "120Hz AMOLED display"
        ],
        price_range="$1199 - $1399"
    ),
    Video(
        title="Google Pixel 8 Pro Review",
        category="Electronics",
        subcategory="Smartphones",
        duration="9:30",
        views="900K",
        highlights=[
            "AI camera capabilities",
            "Real-world performance test",
            "Software features",
            "Sustainability highlights"
        ],
        transcript_summary="A comprehensive review of Google Pixel 8 Pro...",
        key_features=[
            "Tensor G3 chip",
            "Real Tone photography",
            "7-year updates",
            "Recycled materials"
        ],
        price_range="$999 - $1099"
    ),
    # Fashion - Sneakers
    Video(
        title="Adidas Ultraboost 23 Review",
        category="Fashion",
        subcategory="Sneakers",
        duration="7:50",
        views="500K",
        highlights=[
            "Comfort analysis",
            "Performance for running",
            "Material durability test",
            "Style versatility"
        ],
        transcript_summary="In-depth review of the new Adidas Ultraboost 23...",
        key_features=[
            "Boost midsole technology",
            "Primeknit upper",
            "Lightweight design",
            "Eco-friendly materials"
        ],
        price_range="$180 - $220"
    ),
    Video(
        title="Gucci Fall Collection 2025",
        category="Fashion",
        subcategory="Clothing",
        duration="15:20",
        views="2.3M",
        highlights=[
            "Runway looks",
            "Fabric details",
            "Seasonal colors",
            "Styling tips"
        ],
        transcript_summary="Showcase of Gucci's Fall Collection 2025...",
        key_features=[
            "Luxury fabrics",
            "Bold patterns",
            "Exclusive designs",
            "Seasonal accessories"
        ],
        price_range="$500 - $5000"
    ),
    # Beauty - Skincare and Makeup
    Video(
        title="Winter Skincare Routine",
        category="Beauty",
        subcategory="Skincare",
        duration="10:15",
        views="800K",
        highlights=[
            "Product recommendations",
            "Application techniques",
            "Hydration tips",
            "SPF for winter"
        ],
        transcript_summary="Detailed guide for maintaining healthy skin during winter...",
        key_features=[
            "Moisturizing creams",
            "SPF 50 sunscreen",
            "Soothing serums",
            "Gentle exfoliation"
        ],
        price_range="$15 - $100"
    ),
    Video(
        title="Evening Glam Makeup Tutorial",
        category="Beauty",
        subcategory="Makeup",
        duration="13:45",
        views="1.1M",
        highlights=[
            "Step-by-step guide",
            "Product choices",
            "Blending techniques",
            "Finishing touches"
        ],
        transcript_summary="A tutorial to achieve a flawless evening glam look...",
        key_features=[
            "Smokey eyeshadow",
            "Long-lasting foundation",
            "Bold lipsticks",
            "Highlighter application"
        ],
        price_range="$25 - $200"
    )
]

# Video Listings
video_listings = [
    {"title": "Samsung Galaxy S24 Ultra Features", "views": "1.2M", "rating": 4.8, "platform": "YouTube"},
    {"title": "Google Pixel 8 Pro Review", "views": "900K", "rating": 4.7, "platform": "Instagram"},
    {"title": "Adidas Ultraboost 23 Review", "views": "500K", "rating": 4.5, "platform": "Twitter"},
    {"title": "Gucci Fall Collection 2025", "views": "2.3M", "rating": 4.9, "platform": "YouTube"},
    {"title": "Winter Skincare Routine", "views": "800K", "rating": 4.6, "platform": "Instagram"},
    {"title": "Evening Glam Makeup Tutorial", "views": "1.1M", "rating": 4.8, "platform": "Twitter"},
]

# Video Analytics
video_analytics = [
    {
        "title": "Samsung Galaxy S24 Ultra Features",
        "engagement": {
            "views": "1.2M",
            "likes": "50K",
            "comments": "3.2K",
            "average_watch_time": "8:30"
        },
        "audience": {
            "demographics": {
                "18-24": "30%",
                "25-34": "45%",
                "35-44": "15%",
                "45+": "10%"
            },
            "top_regions": ["US", "UK", "Canada", "Australia"]
        },
        "performance": {
            "retention_rate": "68%",
            "click_through_rate": "4.2%",
            "conversion_rate": "2.8%"
        }
    },
    {
        "title": "Google Pixel 8 Pro Review",
        "engagement": {
            "views": "900K",
            "likes": "40K",
            "comments": "2.5K",
            "average_watch_time": "7:50"
        },
        "audience": {
            "demographics": {
                "18-24": "28%",
                "25-34": "50%",
                "35-44": "12%",
                "45+": "10%"
            },
            "top_regions": ["US", "India", "Germany", "UK"]
        },
        "performance": {
            "retention_rate": "72%",
            "click_through_rate": "4.5%",
            "conversion_rate": "3.0%"
        }
    },
    {
        "title": "Adidas Ultraboost 23 Review",
        "engagement": {
            "views": "500K",
            "likes": "20K",
            "comments": "1.1K",
            "average_watch_time": "6:10"
        },
        "audience": {
            "demographics": {
                "18-24": "35%",
                "25-34": "40%",
                "35-44": "15%",
                "45+": "10%"
            },
            "top_regions": ["US", "Canada", "UK", "Australia"]
        },
        "performance": {
            "retention_rate": "60%",
            "click_through_rate": "3.8%",
            "conversion_rate": "2.5%"
        }
    },
    {
        "title": "Gucci Fall Collection 2025",
        "engagement": {
            "views": "500K",
            "likes": "20K",
            "comments": "1.1K",
            "average_watch_time": "6:10"
        },
        "audience": {
            "demographics": {
                "18-24": "35%",
                "25-34": "40%",
                "35-44": "15%",
                "45+": "10%"
            },
            "top_regions": ["US", "Canada", "UK", "Australia"]
        },
        "performance": {
            "retention_rate": "60%",
            "click_through_rate": "3.8%",
            "conversion_rate": "2.5%"
        }
    },
    {
        "title": "Winter Skincare Routine",
        "engagement": {
            "views": "500K",
            "likes": "20K",
            "comments": "1.1K",
            "average_watch_time": "6:10"
        },
        "audience": {
            "demographics": {
                "18-24": "35%",
                "25-34": "40%",
                "35-44": "15%",
                "45+": "10%"
            },
            "top_regions": ["US", "Canada", "UK", "Australia"]
        },
        "performance": {
            "retention_rate": "60%",
            "click_through_rate": "3.8%",
            "conversion_rate": "2.5%"
        }
    },
    {
        "title": "Evening Glam Makeup Tutorial",
        "engagement": {
            "views": "500K",
            "likes": "20K",
            "comments": "1.1K",
            "average_watch_time": "6:10"
        },
        "audience": {
            "demographics": {
                "18-24": "35%",
                "25-34": "40%",
                "35-44": "15%",
                "45+": "10%"
            },
            "top_regions": ["US", "Canada", "UK", "Australia"]
        },
        "performance": {
            "retention_rate": "60%",
            "click_through_rate": "3.8%",
            "conversion_rate": "2.5%"
        }
    }
]



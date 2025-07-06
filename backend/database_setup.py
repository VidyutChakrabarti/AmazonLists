from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from pymongo.server_api import ServerApi
import logging
import os
import time
from models.listing import ProductListing
from models.analytics import Analytics, SalesPerformance, CustomerBehavior, MarketingMetrics, Demographics
from models.review import RecentReview
from models.videoListing import VideoListing, ProductLink
from models.analyticsVideo import VideoAnalytics, VideoAudience, VideoEngagement, VideoPerformance 
from image_data import(
    sample_products,
    product_listings,
    product_reviews,
    product_analytics,
)
from video_data import(
    sample_videos,
    video_listings,
    video_analytics,
)
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration for retry and timeouts
MAX_RETRIES = 5
INITIAL_RETRY_DELAY = 1
MAX_RETRY_DELAY = 30
TIMEOUT_CONFIG = {
    "connectTimeoutMS": 5000,
    "socketTimeoutMS": 10000
}

def exponential_backoff(attempt):
    """Calculate exponential backoff delay."""
    return min(INITIAL_RETRY_DELAY * (2 ** attempt), MAX_RETRY_DELAY)

def connect_to_mongodb():
    """Establish a MongoDB connection with retries and timeouts."""
    uri = os.getenv("MONGODB_URL")
    if not uri:
        logger.error("MONGODB_URL is not set in the environment.")
        raise ValueError("MONGODB_URL is missing")

    for attempt in range(MAX_RETRIES):
        try:
            logger.info(f"Attempting to connect to MongoDB (Attempt {attempt + 1}/{MAX_RETRIES})")
            client = MongoClient(uri, server_api=ServerApi('1'), **TIMEOUT_CONFIG)
            # Verify connection
            client.admin.command("ping")
            logger.info("Connected to MongoDB successfully")
            return client
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            delay = exponential_backoff(attempt)
            logger.warning(f"Connection failed (Attempt {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.error("Maximum retry attempts reached. Exiting...")
                raise
        except Exception as e:
            logger.error(f"Unexpected error while connecting to MongoDB: {e}")
            raise

def setup_product_database():
    """Setup product reference database with sample data"""
    client = None
    try:
        client = connect_to_mongodb()
        db = client.social_media_products
        
        # Create Collections
        product_collection = db["products"]
        listing_collection = db["listings"]
        analytics_collection = db["analytics"]
        review_collection = db["reviews"]
        video_collection = db["videos"]
        video_listings_collection = db["video_listings"]
        video_analytics_collection = db["video_analytics"]

        # Delete indexes
        product_collection.drop_indexes()
        listing_collection.drop_indexes()
        analytics_collection.drop_indexes()
        review_collection.drop_indexes()
        video_collection.drop_indexes()
        video_listings_collection.drop_indexes()
        video_analytics_collection.drop_indexes()
        
        # Create indexes for products
        product_collection.create_index([("id", ASCENDING)])
        product_collection.create_index([("title", ASCENDING)])
        product_collection.create_index([("category", ASCENDING)])
        product_collection.create_index([("subcategory", ASCENDING)])
        product_collection.create_index([("features", ASCENDING)])
        product_collection.create_index([("price_range", ASCENDING)])
        product_collection.create_index([("created_at", ASCENDING)])
        product_collection.create_index([("updated_at", ASCENDING)])

        # Create indexes for listings
        listing_collection.create_index([("id", ASCENDING), ("product_id", ASCENDING)])
        listing_collection.create_index([("product_id", ASCENDING), ("created_at", ASCENDING)])
        listing_collection.create_index([("price", ASCENDING), ("updated_at", ASCENDING)])
        listing_collection.create_index([("features", ASCENDING), ("title", ASCENDING)])
        listing_collection.create_index([("id", ASCENDING)])
        listing_collection.create_index([("title", ASCENDING)])
        listing_collection.create_index([("price", ASCENDING)])
        listing_collection.create_index([("features", ASCENDING)], name="features_index")

        # Create indexes for analytics
        analytics_collection.create_index([("id", ASCENDING), ("product_id", ASCENDING)])
        analytics_collection.create_index([("product_id", ASCENDING), ("created_at", ASCENDING)])
        analytics_collection.create_index([("id", ASCENDING)])
        analytics_collection.create_index([("product_id", ASCENDING)], unique=True)          
        analytics_collection.create_index([("created_at", ASCENDING)])          
        analytics_collection.create_index([("updated_at", ASCENDING)])         
        analytics_collection.create_index([("sales_performance.total_sales", ASCENDING)])     
        analytics_collection.create_index([("sales_performance.revenue", ASCENDING)])          
        analytics_collection.create_index([("sales_performance.average_price", ASCENDING)])    
        analytics_collection.create_index([("customer_behavior.view_to_purchase_rate", ASCENDING)])  
        analytics_collection.create_index([("customer_behavior.repeat_purchase_rate", ASCENDING)])   
        analytics_collection.create_index([("customer_behavior.average_rating", ASCENDING)])         
        analytics_collection.create_index([("marketing_metrics.click_through_rate", ASCENDING)])    
        analytics_collection.create_index([("marketing_metrics.social_media_engagement", ASCENDING)])

        # Create indexes for review
        review_collection.create_index([("product_id", ASCENDING), ("rating", ASCENDING)])
        review_collection.create_index([("user_id", ASCENDING), ("product_id", ASCENDING)])
        review_collection.create_index([("id", ASCENDING)])      
        review_collection.create_index([("product_id", ASCENDING)])      
        review_collection.create_index([("user_id", ASCENDING)])         
        review_collection.create_index([("rating", ASCENDING)])          
        review_collection.create_index([("title", ASCENDING)])           
        review_collection.create_index([("verified_purchase", ASCENDING)])  
        review_collection.create_index([("created_at", ASCENDING)])   
        review_collection.create_index([("updated_at", ASCENDING)])

        # Create indexes for video
        video_collection.create_index([("title", ASCENDING), ("views", ASCENDING)])
        video_collection.create_index([("views", ASCENDING), ("rating", ASCENDING)])
        video_collection.create_index([("id", ASCENDING)])               
        video_collection.create_index([("title", ASCENDING)])                 
        video_collection.create_index([("category", ASCENDING)])              
        video_collection.create_index([("subcategory", ASCENDING)])           
        video_collection.create_index([("duration", ASCENDING)])              
        video_collection.create_index([("views", ASCENDING)])                 
        video_collection.create_index([("transcript_summary", "text")])       
        video_collection.create_index([("price_range", ASCENDING)])           
        video_collection.create_index([("created_at", ASCENDING)])            
        video_collection.create_index([("updated_at", ASCENDING)])           
        video_collection.create_index([("key_features", ASCENDING)])
        video_collection.create_index([("highlights", ASCENDING)])

        # Create indexes for video listing
        video_listings_collection.create_index([("video_id", ASCENDING), ("id", ASCENDING)])
        video_listings_collection.create_index([("id", ASCENDING)])                  
        video_listings_collection.create_index([("video_id", ASCENDING)], unique=True)                  
        video_listings_collection.create_index([("platform", ASCENDING)])                    
        video_listings_collection.create_index([("title", ASCENDING)])                       
        video_listings_collection.create_index([("views", ASCENDING)])                       
        video_listings_collection.create_index([("rating", ASCENDING)])                      
        video_listings_collection.create_index([("created_at", ASCENDING)])                  
        video_listings_collection.create_index([("updated_at", ASCENDING)])                  
        video_listings_collection.create_index([("product_links.price", ASCENDING)])

        # Create indexes for video analytics
        video_analytics_collection.create_index([("id", ASCENDING), ("video_id", ASCENDING)])
        video_analytics_collection.create_index([("id", ASCENDING), ("video_id", ASCENDING)])
        video_analytics_collection.create_index([("engagement.views", ASCENDING), ("engagement.likes", ASCENDING)])
        video_analytics_collection.create_index([("performance.retention_rate", ASCENDING), ("performance.click_through_rate", ASCENDING)])
        video_analytics_collection.create_index([("id", ASCENDING)])                
        video_analytics_collection.create_index([("video_id", ASCENDING)], unique=True)                
        video_analytics_collection.create_index([("created_at", ASCENDING)])                
        video_analytics_collection.create_index([("updated_at", ASCENDING)])                
        video_analytics_collection.create_index([("engagement.views", ASCENDING)])          
        video_analytics_collection.create_index([("engagement.likes", ASCENDING)])          
        video_analytics_collection.create_index([("engagement.comments", ASCENDING)])       
        video_analytics_collection.create_index([("engagement.average_watch_time", ASCENDING)])  
        video_analytics_collection.create_index([("audience.demographics", ASCENDING)])    
        video_analytics_collection.create_index([("audience.top_regions", ASCENDING)])     
        video_analytics_collection.create_index([("performance.retention_rate", ASCENDING)])  
        video_analytics_collection.create_index([("performance.click_through_rate", ASCENDING)])

        logger.info("All indexes created successfully")

        # Clear Existing Products
        product_collection.delete_many({})
        # Insert Sample Products
        product_collection.insert_many([product.model_dump() for product in sample_products])
        logger.info("sample_products inserted")

        # Clear Existing Product Listings
        listing_collection.delete_many({})

        # Generate sample_product_listings
        sample_product_listings = []
        for listing in product_listings:
            # Fetch the _id of the product from the database
            result = product_collection.find_one({"title": listing["title"]}, {"_id": 1})
            
            if result:
                sample_product_listings.append(
                    ProductListing(
                        product_id=str(result["_id"]),
                        title=listing["title"],
                        price=listing["price"],
                        description=listing["description"],
                        features=listing["features"]
                    )
                )
        
        # Insert sample_product_listings 
        listing_collection.insert_many([listing.model_dump() for listing in sample_product_listings])
        logger.info("sample_product_listings inserted")

        # Clear Existing Analytics
        analytics_collection.delete_many({})

        # Generate sample_product_analytics
        sample_product_analytics = [] 
        for analytic in product_analytics:  
            # Fetch the _id of the product from the database
            result = product_collection.find_one({"title": analytic["title"]}, {"_id": 1})
            
            if result:
                sample_product_analytics.append(
                    Analytics(
                        product_id=str(result["_id"]),
                        sales_performance=SalesPerformance(
                            total_sales=analytic["sales_performance"]["total_sales"],
                            revenue=analytic["sales_performance"]["revenue"],
                            average_price=analytic["sales_performance"]["average_price"],
                            growth_rate=analytic["sales_performance"]["growth_rate"]
                        ),
                        customer_behavior=CustomerBehavior(
                            view_to_purchase_rate=analytic["customer_behavior"]["view_to_purchase_rate"],
                            cart_abandonment_rate=analytic["customer_behavior"]["cart_abandonment_rate"],
                            repeat_purchase_rate=analytic["customer_behavior"]["repeat_purchase_rate"],
                            average_rating=analytic["customer_behavior"]["average_rating"]
                        ),
                        demographics=Demographics(
                            age_groups=analytic["demographics"]["age_groups"],
                            top_locations=analytic["demographics"]["top_locations"]
                        ),
                        marketing_metrics=MarketingMetrics(
                            click_through_rate=analytic["marketing_metrics"]["click_through_rate"],
                            conversion_rate=analytic["marketing_metrics"]["conversion_rate"],
                            return_on_ad_spend=analytic["marketing_metrics"]["return_on_ad_spend"],
                            social_media_engagement=analytic["marketing_metrics"]["social_media_engagement"]
                        )
                    )
                )
        
        # Insert sample_product_analytics
        analytics_collection.insert_many([analytic.model_dump() for analytic in sample_product_analytics])
        logger.info("sample_product_analytics inserted")

        # Clear Existing Reviews
        review_collection.delete_many({})

        # Generate sample_reviews
        sample_reviews = []
        for review in product_reviews: 
            # Fetch the _id of the product from the database
            result = product_collection.find_one({"title": review["product_title"]}, {"_id": 1})
            if result:
                sample_reviews.append(
                    RecentReview(
                        product_id=str(result["_id"]),
                        user_id=review["user_id"],
                        rating=review["rating"],
                        title=review["title"],
                        comment=review["comment"],
                        verified_purchase=review["verified_purchase"]
                    )
                )
        # Insert sample_reviews
        review_collection.insert_many([review.model_dump() for review in sample_reviews])
        logger.info("sample_reviews inserted")

        # Clear Existing Videos
        video_collection.delete_many({})
        # Insert sample_videos
        video_collection.insert_many([video.model_dump() for video in sample_videos])
        logger.info("sample_videos inserted")        

        # Clear Existing video_listings
        video_listings_collection.delete_many({})

        # Generate sample_video_listings
        sample_video_listings = []
        for video_listing in video_listings:
            # Fetch the _id of the video from the database
            result = video_collection.find_one({"title": video_listing["title"]}, {"_id": 1})
            if result:
                sample_video_listings.append(
                    VideoListing(
                        video_id=str(result["_id"]),
                        platform=video_listing["platform"],
                        title=video_listing["title"],
                        views=video_listing["views"],
                        rating=video_listing["rating"],
                        key_timestamps={
                            "00:00": "Introduction",
                            "02:00": "Main features",
                            "04:00": "Conclusion"
                        },
                        product_links=[
                            ProductLink(store="Amazon", price="$199"),
                            ProductLink(store="Best Buy", price="$205"),
                        ]
                    )
                )
        # Insert sample_video_listings
        video_listings_collection.insert_many([video_listing.model_dump() for video_listing in sample_video_listings])
        logger.info("sample_video_listings inserted")

        # Clear Existing video_analytics
        video_analytics_collection.delete_many({}) 

        # Generate sample_video_analytics
        sample_video_analytics = []
        for video_analytic in video_analytics:
            # Fetch the _id of the video from the database
            result = video_collection.find_one({"title": video_analytic["title"]}, {"_id": 1})
            if result:
                analytics = VideoAnalytics(
                    video_id=str(result["_id"]),
                    engagement=VideoEngagement(**video_analytic["engagement"]),
                    audience=VideoAudience(**video_analytic["audience"]),
                    performance=VideoPerformance(**video_analytic["performance"])
                )
                sample_video_analytics.append(analytics)

        # Insert sample_video_analytics
        video_analytics_collection.insert_many([video_analytic.model_dump() for video_analytic in sample_video_analytics])
        logger.info("sample_video_analytics inserted")

    except Exception as e:
        logger.error(f"Error setting up database: {e}")
        raise
    finally:
        if client:
            client.close()
            logger.info("MongoDB connection closed")

if __name__ == "__main__":
    setup_product_database()
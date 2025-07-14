import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class ContentProcessor:
    def __init__(self, db, image_processor):
        self.db = db
        self.image_processor = image_processor
    
    async def process_content(self, analysis: Dict, caption: Optional[str] = None) -> Dict:
        """Process analyzed content and generate listing"""
        try:
            # Find matching product reference
            product = await self.find_matching_product(analysis['product_name'])
            
            if not product:
                return None
            
            # Generate listing
            listing = {
                'product_id': str(product['_id']),
                'title': analysis['product_name'],
                'category': product['category'],
                'subcategory': product['subcategory'],
                'description': analysis['description'],
                'price': analysis['price'],
                'features': analysis['key_features'],
                'keywords': analysis['search_keywords'],
                'original_caption': caption,
                'created_at': datetime.utcnow(),
                'status': 'active'
            }
            
            # Save listing
            result = await self.db.listings.insert_one(listing)
            listing['_id'] = str(result.inserted_id)
            
            return listing
            
        except Exception as e:
            logger.error(f"Error processing content: {e}")
            return None
    
    async def find_matching_product(self, title: str) -> Optional[Dict]:
        """Find matching product in reference database"""
        try:
            # Search by exact title match first
            product = await self.db.product_references.find_one({
                "brand_options": {"$regex": title, "$options": "i"}
            })
            
            if not product:
                # Try partial match
                product = await self.db.product_references.find_one({
                    "$or": [
                        {"category": {"$regex": title, "$options": "i"}},
                        {"subcategory": {"$regex": title, "$options": "i"}},
                        {"keywords": {"$regex": title, "$options": "i"}}
                    ]
                })
            
            return product
            
        except Exception as e:
            logger.error(f"Error finding matching product: {e}")
            return None
    
    async def search_products(self, title: str) -> List[Dict]:
        """Search for products by title"""
        try:
            cursor = self.db.product_references.find({
                "$or": [
                    {"brand_options": {"$regex": title, "$options": "i"}},
                    {"category": {"$regex": title, "$options": "i"}},
                    {"subcategory": {"$regex": title, "$options": "i"}},
                    {"keywords": {"$regex": title, "$options": "i"}}
                ]
            }).limit(10)
            
            return await cursor.to_list(length=10)
            
        except Exception as e:
            logger.error(f"Error searching products: {e}")
            return []
    
    async def get_product_listings(self, product_id: str) -> List[Dict]:
        """Get all listings for a product"""
        try:
            cursor = self.db.listings.find({
                "product_id": product_id
            }).sort("created_at", -1)
            
            return await cursor.to_list(length=10)
            
        except Exception as e:
            logger.error(f"Error getting product listings: {e}")
            return []
    
    async def get_comparable_products(self, product_id: str, limit: int = 5) -> List[Dict]:
        """Get comparable products for comparison"""
        try:
            # Get original product
            product = await self.db.product_references.find_one({
                "_id": product_id
            })
            
            if not product:
                return []
            
            # Find products in same category
            cursor = self.db.product_references.find({
                "category": product["category"],
                "subcategory": product["subcategory"],
                "_id": {"$ne": product_id}
            }).limit(limit)
            
            comparables = await cursor.to_list(length=limit)
            
            # Format response
            return [{
                "id": str(p["_id"]),
                "name": p["subcategory"],
                "category": p["category"],
                "price_range": p["price_ranges"],
                "features": p["common_features"][:3]
            } for p in comparables]
            
        except Exception as e:
            logger.error(f"Error getting comparable products: {e}")
            return []

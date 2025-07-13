from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class ProductLink(BaseModel):
    store: str
    price: str

class KeyTimestamp(BaseModel):
    timestamp: str
    description: str

class VideoListing(BaseModel):
    video_id: str
    platform: str
    title: str
    views: str
    rating: float
    key_timestamps: Dict[str, str]
    product_links: List[ProductLink]
    created_at: Optional[str] = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()


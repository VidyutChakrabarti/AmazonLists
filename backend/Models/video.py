from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Video(BaseModel):
    id: Optional[str] = None
    title: str
    category: str
    subcategory: str
    duration: str
    views: str
    highlights: List[str]
    transcript_summary: str
    key_features: List[str]
    price_range: str
    created_at: Optional[str] = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()
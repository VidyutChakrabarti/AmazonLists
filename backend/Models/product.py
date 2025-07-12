from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    id: Optional[str] = None
    title: str
    category: str
    subcategory: str
    features: List[str]
    price_range: str
    created_at: Optional[str] = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()

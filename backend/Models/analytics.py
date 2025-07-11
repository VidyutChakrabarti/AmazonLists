from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime

# Define the nested models
class SalesPerformance(BaseModel):
    total_sales: str
    revenue: str
    average_price: str
    growth_rate: str

class CustomerBehavior(BaseModel):
    view_to_purchase_rate: str
    cart_abandonment_rate: str
    repeat_purchase_rate: str
    average_rating: float

class Demographics(BaseModel):
    age_groups: Dict[str, str]
    top_locations: List[str]

class MarketingMetrics(BaseModel):
    click_through_rate: str
    conversion_rate: str
    return_on_ad_spend: str
    social_media_engagement: str

# Main Analytics model
class Analytics(BaseModel):
    product_id: str
    sales_performance: SalesPerformance
    customer_behavior: CustomerBehavior
    demographics: Demographics
    marketing_metrics: MarketingMetrics
    created_at: Optional[str] = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()

from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import datetime

class VideoEngagement(BaseModel):
    views: str
    likes: str
    comments: str
    average_watch_time: str

class VideoAudience(BaseModel):
    demographics: Dict[str, str]
    top_regions: List[str]

class VideoPerformance(BaseModel):
    retention_rate: str
    click_through_rate: str
    conversion_rate: str

class VideoAnalytics(BaseModel):
    video_id: str
    engagement: VideoEngagement
    audience: VideoAudience
    performance: VideoPerformance
    created_at: Optional[str] = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()

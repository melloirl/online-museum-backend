from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl


class ImageContentBase(BaseModel):
    """Base schema for image content shared properties"""

    image_url: HttpUrl
    description: str
    page_url: Optional[HttpUrl] = None


class ImageContentCreate(ImageContentBase):
    """Schema for creating new image content"""

    pass


class ImageContentUpdate(BaseModel):
    """Schema for updating image content"""

    image_url: Optional[HttpUrl] = None
    description: Optional[str] = None
    page_url: Optional[HttpUrl] = None


class ImageContentResponse(ImageContentBase):
    """Schema for image content responses"""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """Configure Pydantic to handle SQLAlchemy models"""

        from_attributes = True

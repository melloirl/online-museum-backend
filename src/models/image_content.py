from typing import Optional
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class ImageContent(Base):
    """Model for storing image content with descriptions and optional page URLs"""
    __tablename__ = "image_contents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    page_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    def __repr__(self) -> str:
        return f"<ImageContent {self.id}>"

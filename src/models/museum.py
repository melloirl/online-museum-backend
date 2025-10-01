from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Artist(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    biography: Mapped[str] = mapped_column(Text, nullable=True)
    birth_date: Mapped[Optional[datetime]] = mapped_column(Date, nullable=True)
    death_date: Mapped[Optional[datetime]] = mapped_column(Date, nullable=True)
    nationality: Mapped[str] = mapped_column(String(50), nullable=True)

    # Relationships
    artworks: Mapped[List["Artwork"]] = relationship("Artwork", back_populates="artist")

    def __repr__(self) -> str:
        return f"<Artist {self.name}>"


class Artwork(Base):
    __tablename__ = "artworks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    year_created: Mapped[Optional[int]] = mapped_column(nullable=True)
    medium: Mapped[str] = mapped_column(String(100), nullable=True)
    dimensions: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    image_url: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # Foreign Keys
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"), nullable=False)
    
    # Relationships
    artist: Mapped["Artist"] = relationship("Artist", back_populates="artworks")

    def __repr__(self) -> str:
        return f"<Artwork {self.title}>"

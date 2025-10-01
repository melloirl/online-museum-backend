from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.config import get_db
from ..models.image_content import ImageContent
from ..schemas.image_content import (
    ImageContentCreate,
    ImageContentUpdate,
    ImageContentResponse
)

router = APIRouter(
    prefix="/api/images",
    tags=["images"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ImageContentResponse, status_code=status.HTTP_201_CREATED)
def create_image(
    image: ImageContentCreate,
    db: Session = Depends(get_db)
) -> ImageContent:
    """Create a new image content entry"""
    db_image = ImageContent(
        image_url=str(image.image_url),
        description=image.description,
        page_url=str(image.page_url) if image.page_url else None
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

@router.get("/{image_id}", response_model=ImageContentResponse)
def read_image(
    image_id: int,
    db: Session = Depends(get_db)
) -> ImageContent:
    """Get a specific image content by ID"""
    db_image = db.query(ImageContent).filter(ImageContent.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.get("/", response_model=List[ImageContentResponse])
def list_images(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[ImageContent]:
    """List all image content with pagination"""
    return db.query(ImageContent).offset(skip).limit(limit).all()

@router.patch("/{image_id}", response_model=ImageContentResponse)
def update_image(
    image_id: int,
    image: ImageContentUpdate,
    db: Session = Depends(get_db)
) -> ImageContent:
    """Update an image content entry"""
    db_image = db.query(ImageContent).filter(ImageContent.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Update only provided fields
    update_data = image.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        # Convert HttpUrl to string for storage
        if field in ['image_url', 'page_url'] and value is not None:
            value = str(value)
        setattr(db_image, field, value)
    
    db.commit()
    db.refresh(db_image)
    return db_image

@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image(
    image_id: int,
    db: Session = Depends(get_db)
) -> None:
    """Delete an image content entry"""
    db_image = db.query(ImageContent).filter(ImageContent.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    
    db.delete(db_image)
    db.commit()

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from ..database.config import get_db
from ..models.image_content import ImageContent
from ..services.qr_service import QRService

qr = QRService()

router = APIRouter(
    prefix="/museum",
    tags=["museum"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="templates")


@router.get("/{image_id}")
def museum_entry(image_id: int, request: Request, db: Session = Depends(get_db)):
    """Render a page for a given museum entry (image + title + description)."""
    db_image = db.query(ImageContent).filter(ImageContent.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Museum entry not found")

    qr_code = qr.generate_qr(str(request.url))

    return templates.TemplateResponse(
        "museum_entry.html",
        {
            "request": request,
            "title": db_image.title,
            "description": db_image.description,
            "image_url": db_image.image_url,
            "qr_code": qr_code,
        },
    )

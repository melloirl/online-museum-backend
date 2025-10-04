from sqlalchemy.orm import Session
from src.database.config import SessionLocal
from src.models.image_content import ImageContent


def seed_image_content(db: Session):
    """Seed the ImageContent table with sample entries if not already present."""
    if db.query(ImageContent).count() > 0:
        print("ImageContent table already seeded. Skipping.")
        return

    samples = [
        ImageContent(
            image_url="https://example.com/images/art1.jpg",
            description="A vibrant digital painting representing modern abstract art.",
            page_url="https://museumonline.com/artworks/art1",
        ),
        ImageContent(
            image_url="https://example.com/images/art2.jpg",
            description="Black and white photograph capturing urban life in the 20th century.",
            page_url="https://museumonline.com/artworks/art2",
        ),
    ]

    db.add_all(samples)
    db.commit()
    print("✅ Seeded ImageContent with sample entries.")


if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_image_content(db)
    finally:
        db.close()

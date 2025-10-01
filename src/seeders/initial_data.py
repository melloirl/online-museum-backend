from datetime import datetime
from src.models.museum import Artist, Artwork
from src.database.config import SessionLocal

def seed_data() -> None:
    db = SessionLocal()
    try:
        # Create sample artists
        van_gogh = Artist(
            name="Vincent van Gogh",
            biography="Dutch post-impressionist painter who posthumously became one of the most famous and influential figures in Western art history.",
            birth_date=datetime(1853, 3, 30),
            death_date=datetime(1890, 7, 29),
            nationality="Dutch"
        )
        
        da_vinci = Artist(
            name="Leonardo da Vinci",
            biography="Italian polymath of the Renaissance whose areas of interest included invention, drawing, painting, sculpture, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, paleontology, and cartography.",
            birth_date=datetime(1452, 4, 15),
            death_date=datetime(1519, 5, 2),
            nationality="Italian"
        )

        db.add_all([van_gogh, da_vinci])
        db.flush()  # Flush to get the IDs

        # Create sample artworks
        artworks = [
            Artwork(
                title="The Starry Night",
                description="An oil on canvas painting depicting a night scene of a village with a prominent church spire under a swirling sky.",
                year_created=1889,
                medium="Oil on canvas",
                dimensions="73.7 × 92.1 cm",
                image_url="https://example.com/starry-night.jpg",
                artist_id=van_gogh.id
            ),
            Artwork(
                title="Mona Lisa",
                description="A half-length portrait painting of a woman which has been described as the most famous painting in the world.",
                year_created=1503,
                medium="Oil on poplar panel",
                dimensions="77 × 53 cm",
                image_url="https://example.com/mona-lisa.jpg",
                artist_id=da_vinci.id
            ),
            Artwork(
                title="Sunflowers",
                description="A series of still life paintings featuring sunflowers in a vase.",
                year_created=1888,
                medium="Oil on canvas",
                dimensions="92.1 × 73 cm",
                image_url="https://example.com/sunflowers.jpg",
                artist_id=van_gogh.id
            )
        ]

        db.add_all(artworks)
        db.commit()
        print("Sample data has been seeded successfully!")

    except Exception as e:
        print(f"An error occurred while seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()

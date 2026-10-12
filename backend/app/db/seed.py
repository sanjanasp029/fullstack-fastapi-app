from app.core.security import get_password_hash
from app.db.session import SessionLocal
from app.models.catalog import Brand, Category, Product
from app.models.user import User


def seed_demo_data() -> None:
    db = SessionLocal()
    try:
        if db.query(Category).count() == 0:
            db.add_all([
                Category(name="Dark Chocolate", description="Rich cocoa-forward chocolate"),
                Category(name="Milk Chocolate", description="Smooth and creamy chocolate"),
                Category(name="Truffles", description="Luxurious confectionery"),
            ])
        if db.query(Brand).count() == 0:
            db.add_all([
                Brand(name="Cocoa Delights", description="Luxury artisan chocolate"),
                Brand(name="Velvet Creek", description="Crafted confections"),
            ])
        if db.query(User).filter(User.email == "admin@chocolateshop.com").first() is None:
            db.add(User(name="Admin", email="admin@chocolateshop.com", phone="0000000000", hashed_password=get_password_hash("admin123"), is_admin=True))
        db.commit()
        if db.query(Product).count() == 0:
            dark = db.query(Category).filter(Category.name == "Dark Chocolate").first()
            brand = db.query(Brand).filter(Brand.name == "Cocoa Delights").first()
            db.add(Product(name="Dark Cocoa Truffle", description="Smooth dark chocolate truffle", price=18.9, original_price=24.9, stock=25, image_url="https://images.unsplash.com/photo-1511381939415-e44015466834", category_id=dark.id, brand_id=brand.id, is_featured=True, is_bestseller=True, rating=4.8))
        db.commit()
    finally:
        db.close()

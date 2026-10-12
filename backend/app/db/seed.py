from app.db.session import SessionLocal
from app.models.product import Brand, Category, Product
from app.models.user import User
from app.core.security import get_password_hash


def seed_data() -> None:
    db = SessionLocal()
    try:
        if db.query(Category).count() == 0:
            categories = [
                Category(name="Dark Chocolate", description="Rich, cocoa-forward chocolate"),
                Category(name="Milk Chocolate", description="Smooth and creamy chocolate"),
                Category(name="White Chocolate", description="Sweet and creamy vanilla notes"),
                Category(name="Truffles", description="Luxurious premium truffles"),
                Category(name="Gift Boxes", description="Gift-ready selections"),
            ]
            db.add_all(categories)

        if db.query(Brand).count() == 0:
            brands = [
                Brand(name="Cocoa Delights", description="Premium handcrafted chocolate"),
                Brand(name="Luna Bites", description="Luxury artisan chocolate"),
                Brand(name="Velvet Creek", description="European-style confectionery"),
            ]
            db.add_all(brands)

        if db.query(User).filter(User.email == "admin@chocolateshop.com").first() is None:
            db.add(User(name="Admin", email="admin@chocolateshop.com", phone="1234567890", hashed_password=get_password_hash("admin123"), is_admin=True))

        if db.query(Product).count() == 0:
            category = db.query(Category).filter(Category.name == "Dark Chocolate").first()
            brand = db.query(Brand).filter(Brand.name == "Cocoa Delights").first()
            db.add_all([
                Product(name="Dark Cocoa Truffle", description="Smooth dark chocolate truffle assortment", price=18.90, original_price=24.90, stock=25, image_url="https://images.unsplash.com/photo-1578985545062-69928b1d9587", category_id=category.id, brand_id=brand.id, is_featured=True, is_bestseller=True, rating=4.8),
                Product(name="Hazelnut Praline Bar", description="Crisp Hazelnut dark chocolate bar", price=14.50, original_price=19.00, stock=20, image_url="https://images.unsplash.com/photo-1551024601-bec78aea704b", category_id=category.id, brand_id=brand.id, rating=4.6),
                Product(name="Velvet Milk Selection", description="Creamy milk chocolate gift pack", price=22.00, original_price=29.90, stock=18, image_url="https://images.unsplash.com/photo-1511381939415-e44015466834", category_id=db.query(Category).filter(Category.name == "Milk Chocolate").first().id, brand_id=db.query(Brand).filter(Brand.name == "Velvet Creek").first().id, is_featured=True, rating=4.7),
            ])

        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
    print("Seed data loaded.")

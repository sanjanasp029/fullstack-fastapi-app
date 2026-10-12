from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.models.product import Product
from app.models.wishlist import WishlistItem

router = APIRouter()


@router.get("")
def get_wishlist(current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    items = db.query(WishlistItem).filter(WishlistItem.user_id == current_user.id).all()
    return [{"id": i.id, "product_id": i.product_id, "product": db.query(Product).filter(Product.id == i.product_id).first()} for i in items]


@router.post("")
def add_to_wishlist(product_id: int, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not db.query(Product).filter(Product.id == product_id).first():
        raise HTTPException(status_code=404, detail="Product not found")
    existing = db.query(WishlistItem).filter(WishlistItem.user_id == current_user.id, WishlistItem.product_id == product_id).first()
    if existing:
        return {"message": "Already in wishlist"}
    item = WishlistItem(user_id=current_user.id, product_id=product_id)
    db.add(item)
    db.commit()
    return {"message": "Added to wishlist"}


@router.delete("/{product_id}")
def remove_from_wishlist(product_id: int, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    item = db.query(WishlistItem).filter(WishlistItem.user_id == current_user.id, WishlistItem.product_id == product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Product not found in wishlist")
    db.delete(item)
    db.commit()
    return {"message": "Removed from wishlist"}

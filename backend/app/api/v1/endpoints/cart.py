from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.models.product import Product
from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate, CartItemOut, CartSummary

router = APIRouter()


@router.get("", response_model=CartSummary)
def get_cart(current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    cart_items = []
    subtotal = 0.0
    for item in items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product is None:
            continue
        line_total = product.price * item.quantity
        subtotal += line_total
        cart_items.append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "product_name": product.name,
            "product_price": product.price,
            "subtotal": line_total,
        })
    return {"items": cart_items, "subtotal": subtotal, "total": subtotal}


@router.post("", response_model=CartSummary)
def add_item(payload: CartItemCreate, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if payload.quantity > product.stock:
        raise HTTPException(status_code=400, detail="Not enough stock available")

    cart_item = db.query(CartItem).filter(CartItem.user_id == current_user.id, CartItem.product_id == payload.product_id).first()
    if cart_item:
        cart_item.quantity += payload.quantity
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=payload.product_id, quantity=payload.quantity)
        db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return get_cart(current_user=current_user, db=db)


@router.put("/{item_id}", response_model=CartSummary)
def update_item(item_id: int, payload: CartItemCreate, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if product and payload.quantity > product.stock:
        raise HTTPException(status_code=400, detail="Not enough stock available")
    item.quantity = payload.quantity
    db.commit()
    return get_cart(current_user=current_user, db=db)


@router.delete("/{item_id}", response_model=CartSummary)
def remove_item(item_id: int, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(item)
    db.commit()
    return get_cart(current_user=current_user, db=db)

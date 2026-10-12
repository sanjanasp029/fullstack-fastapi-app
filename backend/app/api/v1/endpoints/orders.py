from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.models.order import Order, OrderItem, Payment
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderOut

router = APIRouter()


@router.get("", response_model=list[OrderOut])
def list_orders(current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == current_user.id).order_by(Order.created_at.desc()).all()
    return orders


@router.post("", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    from app.models.cart import CartItem

    cart_items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    subtotal = 0.0
    order_items = []
    for cart_item in cart_items:
        product = db.query(Product).filter(Product.id == cart_item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {cart_item.product_id} no longer exists")
        if cart_item.quantity > product.stock:
            raise HTTPException(status_code=400, detail=f"Not enough stock for {product.name}")
        subtotal += product.price * cart_item.quantity
        order_items.append({
            "product_id": product.id,
            "quantity": cart_item.quantity,
            "price": product.price,
            "product_name": product.name,
            "product_image": product.image_url,
        })

    tax = round(subtotal * 0.08, 2)
    shipping_fee = 6.99 if subtotal < 50 else 0.0
    total = subtotal + tax + shipping_fee

    order = Order(
        order_number=f"CH-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{current_user.id}",
        user_id=current_user.id,
        subtotal=subtotal,
        shipping_fee=shipping_fee,
        tax=tax,
        discount=0.0,
        total=total,
        shipping_address=payload.shipping_address,
        payment_method=payload.payment_method,
        notes=payload.notes,
    )
    db.add(order)
    db.flush()

    for item in order_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item["product_id"],
            quantity=item["quantity"],
            price=item["price"],
            product_name=item["product_name"],
            product_image=item["product_image"],
        )
        db.add(order_item)
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        if product:
            product.stock = max(0, product.stock - item["quantity"])

    payment = Payment(order_id=order.id, amount=total, currency="usd", status="Pending")
    db.add(payment)

    db.query(CartItem).filter(CartItem.user_id == current_user.id).delete()
    db.commit()
    db.refresh(order)
    return order


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

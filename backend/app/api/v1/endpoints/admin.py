from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_admin_user
from app.db.session import get_db
from app.models.order import Order
from app.models.product import Product
from app.models.user import User

router = APIRouter()


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    total_sales = sum(o.total for o in db.query(Order).all())
    total_orders = db.query(Order).count()
    total_customers = db.query(User).filter(User.is_admin == False).count()
    total_products = db.query(Product).count()
    low_stock = db.query(Product).filter(Product.stock <= 5).count()
    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "total_products": total_products,
        "low_stock": low_stock,
    }


@router.get("/orders")
def admin_orders(db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return db.query(Order).order_by(Order.created_at.desc()).all()


@router.put("/orders/{order_id}/status")
def update_order_status(order_id: int, payload: dict, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = payload.get("status", order.status)
    db.commit()
    return {"message": "Order status updated"}

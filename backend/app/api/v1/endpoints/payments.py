from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_admin_user, get_current_active_user
from app.db.session import get_db
from app.models.catalog import Product
from app.models.order import Order, Payment
from app.models.user import User

router = APIRouter()


@router.get("/checkout")
def payment_checkout(current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.user_id == current_user.id).order_by(Order.created_at.desc()).first()
    if not order:
        return {"status": "no_order"}
    return {"status": "payment_ready", "order_id": order.id, "amount": order.total}


@router.post("/create-session")
def create_payment_session(current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.user_id == current_user.id).order_by(Order.created_at.desc()).first()
    if not order:
        raise HTTPException(status_code=404, detail="No order found")
    payment = db.query(Payment).filter(Payment.order_id == order.id).first()
    if payment:
        payment.status = "Pending"
    db.commit()
    return {"payment_status": "Pending", "order_id": order.id, "session_id": "mock_session_123"}


@router.post("/webhook")
def payment_webhook():
    return {"status": "ok"}

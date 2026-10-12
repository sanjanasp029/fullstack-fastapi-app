from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.models.order import Order, Payment

router = APIRouter()


@router.get("/checkout")
def payment_checkout(current_user=Depends(get_current_active_user), db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.user_id == current_user.id).order_by(Order.created_at.desc()).first()
    if not order:
        return {"status": "no_order"}
    return {"status": "payment_ready", "order_id": order.id, "amount": order.total}

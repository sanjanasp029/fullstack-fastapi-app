from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.models.user import User

router = APIRouter()


@router.get("/me")
def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user

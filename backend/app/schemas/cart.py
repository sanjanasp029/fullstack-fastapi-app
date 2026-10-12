from pydantic import BaseModel, Field


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    product_name: str | None = None
    product_price: float | None = None
    subtotal: float | None = None

    class Config:
        orm_mode = True


class CartSummary(BaseModel):
    items: list[CartItemOut]
    subtotal: float
    total: float

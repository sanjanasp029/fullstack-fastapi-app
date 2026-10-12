from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    shipping_address: str = Field(..., min_length=10)
    payment_method: str = "Card"
    notes: str | None = None


class OrderItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    product_name: str
    product_image: str | None = None

    class Config:
        orm_mode = True


class OrderOut(BaseModel):
    id: int
    order_number: str
    status: str
    payment_status: str
    subtotal: float
    shipping_fee: float
    tax: float
    discount: float
    total: float
    shipping_address: str
    created_at: str | None = None
    items: list[OrderItemOut] = []

    class Config:
        orm_mode = True

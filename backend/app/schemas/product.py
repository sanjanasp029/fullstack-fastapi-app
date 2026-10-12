from pydantic import BaseModel, Field


class CategoryOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True


class BrandOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=10)
    price: float = Field(..., ge=0)
    original_price: float | None = Field(default=None, ge=0)
    stock: int = Field(default=0, ge=0)
    image_url: str | None = None
    category_id: int
    brand_id: int
    is_featured: bool = False
    is_bestseller: bool = False
    ingredients: str | None = None
    allergens: str | None = None
    weight: str | None = None


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    original_price: float | None = None
    stock: int
    image_url: str | None = None
    category_id: int
    brand_id: int
    rating: float = 0.0
    is_featured: bool = False
    is_bestseller: bool = False
    is_active: bool = True
    ingredients: str | None = None
    allergens: str | None = None
    weight: str | None = None

    class Config:
        orm_mode = True


class ProductUpdate(ProductCreate):
    pass

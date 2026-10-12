from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    email: EmailStr
    phone: str | None = None
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    is_admin: bool = False

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

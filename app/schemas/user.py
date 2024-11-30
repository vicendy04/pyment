from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Schemas cho User
class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    balance: Optional[float] = None


class UserResponse(UserBase):
    user_id: int
    created_at: datetime
    balance: float

    class Config:
        # chuyển đổi từ các model SQLAlchemy sang schema.
        orm_mode = True

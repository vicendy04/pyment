from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Schemas cho Merchant
class MerchantBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str] = None


class MerchantCreate(MerchantBase):
    pass


class MerchantUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    balance: Optional[float] = None


class MerchantResponse(MerchantBase):
    merchant_id: int
    created_at: datetime
    balance: float

    class Config:
        orm_mode = True

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


# Enum
class MethodType(str, Enum):
    credit_card = "credit_card"
    bank_account = "bank_account"


# Schemas cho PaymentMethod
class PaymentMethodBase(BaseModel):
    user_id: int
    method_type: MethodType
    details: str


class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethodResponse(PaymentMethodBase):
    payment_method_id: int
    created_at: datetime

    class Config:
        orm_mode = True

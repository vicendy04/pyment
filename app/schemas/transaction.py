from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


# Enum
class TransactionType(str, Enum):
    payment = "payment"
    refund = "refund"


class TransactionStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"


# Schemas cho Transaction
class TransactionBase(BaseModel):
    user_id: int
    merchant_id: int
    amount: float
    transaction_type: TransactionType
    status: TransactionStatus


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    status: Optional[TransactionStatus] = None


class TransactionResponse(TransactionBase):
    transaction_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

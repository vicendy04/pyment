from datetime import datetime

from pydantic import BaseModel


# Schemas cho TransactionLog
class TransactionLogBase(BaseModel):
    transaction_id: int
    event: str


class TransactionLogCreate(TransactionLogBase):
    pass


class TransactionLogResponse(TransactionLogBase):
    log_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

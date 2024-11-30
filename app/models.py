from datetime import datetime

import database as database
from database import Base, engine
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


# User Table
class User(database.Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    phone_number = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    balance = Column(Float, default=0.0)

    # payment_methods = relationship("PaymentMethod", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")


# Merchant Table
class Merchant(database.Base):
    __tablename__ = "merchants"

    merchant_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    balance = Column(Float, default=0.0)

    transactions = relationship("Transaction", back_populates="merchant")


# Transaction Table
class Transaction(database.Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    merchant_id = Column(Integer, ForeignKey("merchants.merchant_id"), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(
        Enum("payment", "refund", name="transaction_type"), nullable=False
    )
    status = Column(
        Enum("pending", "completed", "failed", name="transaction_status"),
        nullable=False,
    )
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    merchant = relationship("Merchant", back_populates="transactions")
    logs = relationship("TransactionLog", back_populates="transaction")


# PaymentMethod Table
# class PaymentMethod(database.Base):
#     __tablename__ = "payment_methods"

#     payment_method_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
#     method_type = Column(
#         Enum("credit_card", "bank_account", name="method_type"), nullable=False
#     )
#     details = Column(Text, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship("User", back_populates="payment_methods")


# TransactionLog Table
class TransactionLog(database.Base):
    __tablename__ = "transaction_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(
        Integer, ForeignKey("transactions.transaction_id"), nullable=False
    )
    event = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    transaction = relationship("Transaction", back_populates="logs")


Base.metadata.create_all(engine)

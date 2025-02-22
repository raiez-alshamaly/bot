from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
from config import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

# جدول المستخدمين
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    referral_link = Column(Text, unique=True)
    balance = Column(DECIMAL(10,2), default=0.00)
    referred_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

# جدول الإداريين
class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    role = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

# جدول المعاملات
class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(DECIMAL(10,2), nullable=False)
    payment_method = Column(String(50))
    status = Column(String(20), default="pending")
    transaction_id = Column(Text, unique=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

# جدول طلبات السحب
class WithdrawRequest(Base):
    __tablename__ = "withdraw_requests"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(DECIMAL(10,2), nullable=False)
    status = Column(String(20), default="pending")
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(engine)

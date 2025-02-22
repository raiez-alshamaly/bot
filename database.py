from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_URL

# إنشاء الاتصال بقاعدة البيانات
engine = create_engine(DB_URL, echo=True)

# تعريف الجلسة
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# تعريف قاعدة البيانات
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    referral_link = Column(String(255), nullable=True)
    balance = Column(Float, default=0.0)

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(bind=engine)

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    category = Column(String, index=True)
    price = Column(Float, nullable=False)
    current_stock = Column(Integer, default=0)
    safety_stock = Column(Integer, default=10)
    reorder_point = Column(Integer, default=20)
    created_at = Column(DateTime, default=datetime.utcnow)
"""Sales domain models: Lead, Customer, Opportunity, Invoice, Order, Quote, Vendor, PurchaseRequest."""
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from ...database import Base


class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    source = Column(String, nullable=True)
    status = Column(String, default="New")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    segment = Column(String, nullable=True)

class Opportunity(Base):
    __tablename__ = "opportunities"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    title = Column(String, nullable=False)
    value = Column(Float, default=0.0)
    stage = Column(String, default="Prospecting")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=True)
    amount = Column(Float, default=0.0)
    status = Column(String, default="Draft")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    total = Column(Float, default=0.0)
    status = Column(String, default="Pending")

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    total = Column(Float, default=0.0)
    valid_until = Column(Date, nullable=True)

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_email = Column(String, nullable=True)
    contract_terms = Column(Text, nullable=True)

class PurchaseRequest(Base):
    __tablename__ = "purchase_requests"
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    description = Column(String, nullable=True)
    amount = Column(Float, default=0.0)
    status = Column(String, default="Pending")

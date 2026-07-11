"""Sales domain Pydantic schemas."""
from pydantic import BaseModel

class LeadRead(BaseModel):
    id: int
    name: str
    status: str
    class Config:
        from_attributes = True

class CustomerRead(BaseModel):
    id: int
    name: str
    segment: str | None = None
    class Config:
        from_attributes = True

class InvoiceRead(BaseModel):
    id: int
    amount: float
    status: str
    class Config:
        from_attributes = True

class OrderRead(BaseModel):
    id: int
    total: float
    status: str
    class Config:
        from_attributes = True

class VendorRead(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class PurchaseRequestRead(BaseModel):
    id: int
    description: str | None = None
    amount: float
    status: str
    class Config:
        from_attributes = True

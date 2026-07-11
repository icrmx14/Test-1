"""Sales domain Pydantic schemas."""
from pydantic import BaseModel
from datetime import date


class LeadCreate(BaseModel):
    name: str
    email: str | None = None
    source: str | None = None
    status: str | None = "New"


class LeadRead(BaseModel):
    id: int
    name: str
    email: str | None = None
    source: str | None = None
    status: str

    class Config:
        from_attributes = True


class CustomerCreate(BaseModel):
    name: str
    email: str | None = None
    segment: str | None = None


class CustomerRead(BaseModel):
    id: int
    name: str
    email: str | None = None
    segment: str | None = None

    class Config:
        from_attributes = True


class OpportunityCreate(BaseModel):
    customer_id: int
    title: str
    value: float | None = 0.0
    stage: str | None = "Prospecting"


class OpportunityRead(BaseModel):
    id: int
    customer_id: int
    title: str
    value: float
    stage: str

    class Config:
        from_attributes = True


class InvoiceCreate(BaseModel):
    order_id: int | None = None
    amount: float
    status: str | None = "Draft"


class InvoiceRead(BaseModel):
    id: int
    order_id: int | None = None
    amount: float
    status: str

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    customer_id: int
    total: float
    status: str | None = "Pending"


class OrderRead(BaseModel):
    id: int
    customer_id: int
    total: float
    status: str

    class Config:
        from_attributes = True


class QuoteCreate(BaseModel):
    customer_id: int
    total: float
    valid_until: date | None = None


class QuoteRead(BaseModel):
    id: int
    customer_id: int
    total: float
    valid_until: date | None = None

    class Config:
        from_attributes = True


class VendorCreate(BaseModel):
    name: str
    contact_email: str | None = None
    contract_terms: str | None = None


class VendorRead(BaseModel):
    id: int
    name: str
    contact_email: str | None = None
    contract_terms: str | None = None

    class Config:
        from_attributes = True


class PurchaseRequestCreate(BaseModel):
    vendor_id: int
    description: str | None = None
    amount: float
    status: str | None = "Pending"


class PurchaseRequestRead(BaseModel):
    id: int
    vendor_id: int
    description: str | None = None
    amount: float
    status: str

    class Config:
        from_attributes = True

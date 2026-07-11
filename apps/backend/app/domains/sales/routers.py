from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database import get_db
from .schemas import (
    LeadCreate, LeadRead,
    CustomerCreate, CustomerRead,
    OpportunityCreate, OpportunityRead,
    InvoiceCreate, InvoiceRead,
    OrderCreate, OrderRead,
    QuoteCreate, QuoteRead,
    VendorCreate, VendorRead,
    PurchaseRequestCreate, PurchaseRequestRead
)
from . import services

router = APIRouter()


@router.get("/leads", response_model=list[LeadRead])
def list_leads(db: Session = Depends(get_db)):
    return services.list_leads(db)


@router.post("/leads", response_model=LeadRead)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    return services.create_lead(db, lead)


@router.get("/customers", response_model=list[CustomerRead])
def list_customers(db: Session = Depends(get_db)):
    return services.list_customers(db)


@router.post("/customers", response_model=CustomerRead)
def create_customer(cust: CustomerCreate, db: Session = Depends(get_db)):
    return services.create_customer(db, cust)


@router.get("/opportunities", response_model=list[OpportunityRead])
def list_opportunities(db: Session = Depends(get_db)):
    return services.list_opportunities(db)


@router.post("/opportunities", response_model=OpportunityRead)
def create_opportunity(opp: OpportunityCreate, db: Session = Depends(get_db)):
    return services.create_opportunity(db, opp)


@router.get("/invoices", response_model=list[InvoiceRead])
def list_invoices(db: Session = Depends(get_db)):
    return services.list_invoices(db)


@router.post("/invoices", response_model=InvoiceRead)
def create_invoice(inv: InvoiceCreate, db: Session = Depends(get_db)):
    return services.create_invoice(db, inv)


@router.get("/orders", response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return services.list_orders(db)


@router.post("/orders", response_model=OrderRead)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return services.create_order(db, order)


@router.get("/quotes", response_model=list[QuoteRead])
def list_quotes(db: Session = Depends(get_db)):
    return services.list_quotes(db)


@router.post("/quotes", response_model=QuoteRead)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    return services.create_quote(db, quote)


@router.get("/vendors", response_model=list[VendorRead])
def list_vendors(db: Session = Depends(get_db)):
    return services.list_vendors(db)


@router.post("/vendors", response_model=VendorRead)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    return services.create_vendor(db, vendor)


@router.get("/purchase-requests", response_model=list[PurchaseRequestRead])
def list_purchase_requests(db: Session = Depends(get_db)):
    return services.list_purchase_requests(db)


@router.post("/purchase-requests", response_model=PurchaseRequestRead)
def create_purchase_request(pr: PurchaseRequestCreate, db: Session = Depends(get_db)):
    return services.create_purchase_request(db, pr)


@router.patch("/purchase-requests/{pr_id}/approve", response_model=PurchaseRequestRead)
def approve_purchase_request(pr_id: int, db: Session = Depends(get_db)):
    pr = services.approve_purchase_request(db, pr_id)
    if not pr:
        raise HTTPException(status_code=404, detail="Purchase request not found")
    return pr

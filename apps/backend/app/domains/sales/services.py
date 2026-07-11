from sqlalchemy.orm import Session
from .models import Lead, Customer, Opportunity, Invoice, Order, Quote, Vendor, PurchaseRequest
from .schemas import (
    LeadCreate, CustomerCreate, OpportunityCreate,
    InvoiceCreate, OrderCreate, QuoteCreate, VendorCreate, PurchaseRequestCreate
)


def list_leads(db: Session):
    return db.query(Lead).all()


def create_lead(db: Session, lead: LeadCreate):
    db_lead = Lead(name=lead.name, email=lead.email, source=lead.source, status=lead.status)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


def list_customers(db: Session):
    return db.query(Customer).all()


def create_customer(db: Session, cust: CustomerCreate):
    db_cust = Customer(name=cust.name, email=cust.email, segment=cust.segment)
    db.add(db_cust)
    db.commit()
    db.refresh(db_cust)
    return db_cust


def list_opportunities(db: Session):
    return db.query(Opportunity).all()


def create_opportunity(db: Session, opp: OpportunityCreate):
    db_opp = Opportunity(customer_id=opp.customer_id, title=opp.title, value=opp.value, stage=opp.stage)
    db.add(db_opp)
    db.commit()
    db.refresh(db_opp)
    return db_opp


def list_invoices(db: Session):
    return db.query(Invoice).all()


def create_invoice(db: Session, inv: InvoiceCreate):
    db_inv = Invoice(order_id=inv.order_id, amount=inv.amount, status=inv.status)
    db.add(db_inv)
    db.commit()
    db.refresh(db_inv)
    return db_inv


def list_orders(db: Session):
    return db.query(Order).all()


def create_order(db: Session, order: OrderCreate):
    db_order = Order(customer_id=order.customer_id, total=order.total, status=order.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Workflow: Reduce Inventory & Check Reorder Point
    from ..operations.models import SKU
    sku = db.query(SKU).first()
    if sku:
        sku.quantity_on_hand = max(0, sku.quantity_on_hand - 5)
        db.commit()

        if sku.quantity_on_hand < sku.reorder_point:
            from .models import PurchaseRequest, Vendor
            vendor = db.query(Vendor).first()
            if vendor:
                db_pr = PurchaseRequest(
                    vendor_id=vendor.id,
                    description=f"Auto-generated request for low-stock SKU: {sku.name}",
                    amount=float(sku.reorder_point * 20.0),
                    status="Pending"
                )
                db.add(db_pr)
                db.commit()
    return db_order


def list_quotes(db: Session):
    return db.query(Quote).all()


def create_quote(db: Session, quote: QuoteCreate):
    db_quote = Quote(customer_id=quote.customer_id, total=quote.total, valid_until=quote.valid_until)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote


def list_vendors(db: Session):
    return db.query(Vendor).all()


def create_vendor(db: Session, vendor: VendorCreate):
    db_vendor = Vendor(name=vendor.name, contact_email=vendor.contact_email, contract_terms=vendor.contract_terms)
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor


def list_purchase_requests(db: Session):
    return db.query(PurchaseRequest).all()


def create_purchase_request(db: Session, pr: PurchaseRequestCreate):
    db_pr = PurchaseRequest(vendor_id=pr.vendor_id, description=pr.description, amount=pr.amount, status=pr.status)
    db.add(db_pr)
    db.commit()
    db.refresh(db_pr)
    return db_pr


def approve_purchase_request(db: Session, pr_id: int):
    pr = db.query(PurchaseRequest).filter(PurchaseRequest.id == pr_id).first()
    if pr:
        pr.status = "Approved"
        from ..operations.models import SKU
        sku = db.query(SKU).first()
        if sku:
            sku.quantity_on_hand += 50
        db.commit()
        db.refresh(pr)
    return pr

from fastapi import APIRouter

router = APIRouter()

@router.get("/leads")
def list_leads():
    return []

@router.post("/leads")
def create_lead():
    return {"detail": "stub"}

@router.get("/customers")
def list_customers():
    return []

@router.post("/customers")
def create_customer():
    return {"detail": "stub"}

@router.get("/opportunities")
def list_opportunities():
    return []

@router.get("/invoices")
def list_invoices():
    return []

@router.post("/invoices")
def create_invoice():
    return {"detail": "stub"}

@router.get("/orders")
def list_orders():
    return []

@router.post("/orders")
def create_order():
    return {"detail": "stub"}

@router.get("/quotes")
def list_quotes():
    return []

@router.get("/vendors")
def list_vendors():
    return []

@router.post("/vendors")
def create_vendor():
    return {"detail": "stub"}

@router.get("/purchase-requests")
def list_purchase_requests():
    return []

@router.post("/purchase-requests")
def create_purchase_request():
    return {"detail": "stub"}

from fastapi import APIRouter

router = APIRouter()

@router.get("/skus")
def list_skus():
    return []

@router.post("/skus")
def create_sku():
    return {"detail": "stub"}

@router.post("/stock-adjustments")
def adjust_stock():
    return {"detail": "stub"}

@router.get("/warehouses")
def list_warehouses():
    return []

@router.post("/warehouses")
def create_warehouse():
    return {"detail": "stub"}

@router.post("/stock-transfers")
def create_stock_transfer():
    return {"detail": "stub"}

@router.get("/bom")
def list_bom():
    return []

@router.get("/assets")
def list_assets():
    return []

@router.post("/assets")
def create_asset():
    return {"detail": "stub"}

@router.get("/quality-defects")
def list_quality_defects():
    return []

@router.post("/quality-defects")
def create_quality_defect():
    return {"detail": "stub"}

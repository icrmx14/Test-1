from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from .schemas import (
    SKUCreate, SKURead,
    WarehouseCreate, WarehouseRead,
    StockTransferCreate, StockTransferRead,
    BillOfMaterialsCreate, BillOfMaterialsRead,
    AssetCreate, AssetRead,
    QualityDefectCreate, QualityDefectRead
)
from . import services

router = APIRouter()


@router.get("/skus", response_model=list[SKURead])
def list_skus(db: Session = Depends(get_db)):
    return services.list_skus(db)


@router.post("/skus", response_model=SKURead)
def create_sku(sku: SKUCreate, db: Session = Depends(get_db)):
    return services.create_sku(db, sku)


@router.post("/stock-adjustments")
def adjust_stock(sku_id: int, quantity: int, db: Session = Depends(get_db)):
    sku = services.adjust_stock(db, sku_id, quantity)
    if not sku:
        raise HTTPException(status_code=404, detail="SKU not found")
    return {"status": "success", "sku_id": sku_id, "quantity_on_hand": quantity}


@router.get("/warehouses", response_model=list[WarehouseRead])
def list_warehouses(db: Session = Depends(get_db)):
    return services.list_warehouses(db)


@router.post("/warehouses", response_model=WarehouseRead)
def create_warehouse(wh: WarehouseCreate, db: Session = Depends(get_db)):
    return services.create_warehouse(db, wh)


@router.post("/stock-transfers", response_model=StockTransferRead)
def create_stock_transfer(transfer: StockTransferCreate, db: Session = Depends(get_db)):
    db_transfer = services.transfer_stock(db, transfer)
    if not db_transfer:
        raise HTTPException(status_code=404, detail="SKU or Warehouse not found")
    return db_transfer


@router.get("/bom", response_model=list[BillOfMaterialsRead])
def list_bom(db: Session = Depends(get_db)):
    return services.list_bom(db)


@router.post("/bom", response_model=BillOfMaterialsRead)
def create_bom(bom: BillOfMaterialsCreate, db: Session = Depends(get_db)):
    return services.create_bom(db, bom)


@router.get("/assets", response_model=list[AssetRead])
def list_assets(db: Session = Depends(get_db)):
    return services.list_assets(db)


@router.post("/assets", response_model=AssetRead)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    return services.create_asset(db, asset)


@router.get("/quality-defects", response_model=list[QualityDefectRead])
def list_quality_defects(db: Session = Depends(get_db)):
    return services.list_quality_defects(db)


@router.post("/quality-defects", response_model=QualityDefectRead)
def create_quality_defect(qd: QualityDefectCreate, db: Session = Depends(get_db)):
    return services.log_quality_defect(db, qd)

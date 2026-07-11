from sqlalchemy.orm import Session
from .models import SKU, Warehouse, StockTransfer, BillOfMaterials, Asset, QualityDefect
from .schemas import (
    SKUCreate, WarehouseCreate, StockTransferCreate,
    BillOfMaterialsCreate, AssetCreate, QualityDefectCreate
)


def list_skus(db: Session):
    return db.query(SKU).all()


def create_sku(db: Session, sku: SKUCreate):
    db_sku = SKU(
        code=sku.code,
        name=sku.name,
        category=sku.category,
        batch_number=sku.batch_number,
        serial_number=sku.serial_number,
        reorder_point=sku.reorder_point,
        quantity_on_hand=sku.quantity_on_hand
    )
    db.add(db_sku)
    db.commit()
    db.refresh(db_sku)
    return db_sku


def adjust_stock(db: Session, sku_id: int, qty: int):
    sku = db.query(SKU).filter(SKU.id == sku_id).first()
    if sku:
        sku.quantity_on_hand = qty
        db.commit()
        db.refresh(sku)
    return sku


def list_warehouses(db: Session):
    return db.query(Warehouse).all()


def create_warehouse(db: Session, wh: WarehouseCreate):
    db_wh = Warehouse(name=wh.name, location=wh.location)
    db.add(db_wh)
    db.commit()
    db.refresh(db_wh)
    return db_wh


def transfer_stock(db: Session, transfer: StockTransferCreate):
    # Retrieve SKU
    sku = db.query(SKU).filter(SKU.id == transfer.sku_id).first()
    if not sku:
        return None

    # Log transfer record
    db_transfer = StockTransfer(
        sku_id=transfer.sku_id,
        from_warehouse_id=transfer.from_warehouse_id,
        to_warehouse_id=transfer.to_warehouse_id,
        quantity=transfer.quantity
    )
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer


def list_bom(db: Session):
    return db.query(BillOfMaterials).all()


def create_bom(db: Session, bom: BillOfMaterialsCreate):
    db_bom = BillOfMaterials(product_name=bom.product_name, components=bom.components)
    db.add(db_bom)
    db.commit()
    db.refresh(db_bom)
    return db_bom


def list_assets(db: Session):
    return db.query(Asset).all()


def create_asset(db: Session, asset: AssetCreate):
    db_asset = Asset(
        name=asset.name,
        asset_type=asset.asset_type,
        purchase_date=asset.purchase_date,
        depreciation_rate=asset.depreciation_rate,
        warranty_expiry=asset.warranty_expiry
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def log_quality_defect(db: Session, qd: QualityDefectCreate):
    db_qd = QualityDefect(sku_id=qd.sku_id, description=qd.description, severity=qd.severity)
    db.add(db_qd)
    db.commit()
    db.refresh(db_qd)
    return db_qd

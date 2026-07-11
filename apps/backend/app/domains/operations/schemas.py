"""Operations domain Pydantic schemas."""
from pydantic import BaseModel
from datetime import date


class SKUCreate(BaseModel):
    code: str
    name: str
    category: str | None = None
    batch_number: str | None = None
    serial_number: str | None = None
    reorder_point: int | None = 0
    quantity_on_hand: int | None = 0


class SKURead(BaseModel):
    id: int
    code: str
    name: str
    category: str | None = None
    batch_number: str | None = None
    serial_number: str | None = None
    reorder_point: int
    quantity_on_hand: int

    class Config:
        from_attributes = True


class WarehouseCreate(BaseModel):
    name: str
    location: str | None = None


class WarehouseRead(BaseModel):
    id: int
    name: str
    location: str | None = None

    class Config:
        from_attributes = True


class StockTransferCreate(BaseModel):
    sku_id: int
    from_warehouse_id: int
    to_warehouse_id: int
    quantity: int


class StockTransferRead(BaseModel):
    id: int
    sku_id: int
    from_warehouse_id: int
    to_warehouse_id: int
    quantity: int

    class Config:
        from_attributes = True


class BillOfMaterialsCreate(BaseModel):
    product_name: str
    components: str | None = None


class BillOfMaterialsRead(BaseModel):
    id: int
    product_name: str
    components: str | None = None

    class Config:
        from_attributes = True


class AssetCreate(BaseModel):
    name: str
    asset_type: str | None = None
    purchase_date: date | None = None
    depreciation_rate: float | None = 0.0
    warranty_expiry: date | None = None


class AssetRead(BaseModel):
    id: int
    name: str
    asset_type: str | None = None
    purchase_date: date | None = None
    depreciation_rate: float
    warranty_expiry: date | None = None

    class Config:
        from_attributes = True


class QualityDefectCreate(BaseModel):
    sku_id: int | None = None
    description: str | None = None
    severity: str | None = "Low"


class QualityDefectRead(BaseModel):
    id: int
    sku_id: int | None = None
    description: str | None = None
    severity: str

    class Config:
        from_attributes = True

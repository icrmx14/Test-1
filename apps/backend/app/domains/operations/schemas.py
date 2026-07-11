"""Operations domain Pydantic schemas."""
from pydantic import BaseModel

class SKURead(BaseModel):
    id: int
    code: str
    name: str
    category: str | None = None
    quantity_on_hand: int
    reorder_point: int
    class Config:
        from_attributes = True

class WarehouseRead(BaseModel):
    id: int
    name: str
    location: str | None = None
    class Config:
        from_attributes = True

class AssetRead(BaseModel):
    id: int
    name: str
    asset_type: str | None = None
    depreciation_rate: float
    class Config:
        from_attributes = True

class QualityDefectRead(BaseModel):
    id: int
    description: str | None = None
    severity: str
    class Config:
        from_attributes = True

"""Operations domain models: SKU, Warehouse, StockTransfer, BOM, Asset, QualityDefect."""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from ...database import Base


class SKU(Base):
    __tablename__ = "skus"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    batch_number = Column(String, nullable=True)
    serial_number = Column(String, nullable=True)
    reorder_point = Column(Integer, default=0)
    quantity_on_hand = Column(Integer, default=0)

class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)

class StockTransfer(Base):
    __tablename__ = "stock_transfers"
    id = Column(Integer, primary_key=True, index=True)
    sku_id = Column(Integer, ForeignKey("skus.id"))
    from_warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    to_warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    quantity = Column(Integer, default=0)

class BillOfMaterials(Base):
    __tablename__ = "bom"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    components = Column(Text, nullable=True)

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    asset_type = Column(String, nullable=True)
    purchase_date = Column(Date, nullable=True)
    depreciation_rate = Column(Float, default=0.0)
    warranty_expiry = Column(Date, nullable=True)

class QualityDefect(Base):
    __tablename__ = "quality_defects"
    id = Column(Integer, primary_key=True, index=True)
    sku_id = Column(Integer, ForeignKey("skus.id"), nullable=True)
    description = Column(Text, nullable=True)
    severity = Column(String, default="Low")

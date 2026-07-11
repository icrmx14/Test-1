"""Organization domain Pydantic schemas."""
from pydantic import BaseModel


class CompanyRead(BaseModel):
    id: int
    name: str
    address: str | None = None
    class Config:
        from_attributes = True

class BranchRead(BaseModel):
    id: int
    name: str
    company_id: int
    class Config:
        from_attributes = True

class DepartmentRead(BaseModel):
    id: int
    name: str
    branch_id: int
    class Config:
        from_attributes = True

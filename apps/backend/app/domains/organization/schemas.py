"""Organization domain Pydantic schemas."""
from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    address: str | None = None


class CompanyRead(BaseModel):
    id: int
    name: str
    address: str | None = None

    class Config:
        from_attributes = True


class BranchCreate(BaseModel):
    name: str
    company_id: int


class BranchRead(BaseModel):
    id: int
    name: str
    company_id: int

    class Config:
        from_attributes = True


class DepartmentCreate(BaseModel):
    name: str
    branch_id: int


class DepartmentRead(BaseModel):
    id: int
    name: str
    branch_id: int

    class Config:
        from_attributes = True


class TeamCreate(BaseModel):
    name: str
    department_id: int


class TeamRead(BaseModel):
    id: int
    name: str
    department_id: int

    class Config:
        from_attributes = True


class CostCenterCreate(BaseModel):
    name: str
    code: str


class CostCenterRead(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        from_attributes = True

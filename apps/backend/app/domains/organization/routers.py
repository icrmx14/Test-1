from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database import get_db
from .schemas import (
    CompanyCreate, CompanyRead,
    BranchCreate, BranchRead,
    DepartmentCreate, DepartmentRead,
    TeamCreate, TeamRead,
    CostCenterCreate, CostCenterRead
)
from . import services

router = APIRouter()


@router.get("/companies", response_model=list[CompanyRead])
def list_companies(db: Session = Depends(get_db)):
    return services.list_companies(db)


@router.post("/companies", response_model=CompanyRead)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return services.create_company(db, company)


@router.get("/branches", response_model=list[BranchRead])
def list_branches(db: Session = Depends(get_db)):
    return services.list_branches(db)


@router.post("/branches", response_model=BranchRead)
def create_branch(branch: BranchCreate, db: Session = Depends(get_db)):
    return services.create_branch(db, branch)


@router.get("/departments", response_model=list[DepartmentRead])
def list_departments(db: Session = Depends(get_db)):
    return services.list_departments(db)


@router.post("/departments", response_model=DepartmentRead)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    return services.create_department(db, dept)


@router.get("/teams", response_model=list[TeamRead])
def list_teams(db: Session = Depends(get_db)):
    return services.list_teams(db)


@router.post("/teams", response_model=TeamRead)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return services.create_team(db, team)


@router.get("/cost-centers", response_model=list[CostCenterRead])
def list_cost_centers(db: Session = Depends(get_db)):
    return services.list_cost_centers(db)


@router.post("/cost-centers", response_model=CostCenterRead)
def create_cost_center(cc: CostCenterCreate, db: Session = Depends(get_db)):
    return services.create_cost_center(db, cc)

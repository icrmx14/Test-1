from sqlalchemy.orm import Session
from .models import Company, Branch, Department, Team, CostCenter
from .schemas import CompanyCreate, BranchCreate, DepartmentCreate, TeamCreate, CostCenterCreate


def list_companies(db: Session):
    return db.query(Company).all()


def create_company(db: Session, company: CompanyCreate):
    db_company = Company(name=company.name, address=company.address)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def list_branches(db: Session):
    return db.query(Branch).all()


def create_branch(db: Session, branch: BranchCreate):
    db_branch = Branch(name=branch.name, company_id=branch.company_id)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch


def list_departments(db: Session):
    return db.query(Department).all()


def create_department(db: Session, dept: DepartmentCreate):
    db_dept = Department(name=dept.name, branch_id=dept.branch_id)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept


def list_teams(db: Session):
    return db.query(Team).all()


def create_team(db: Session, team: TeamCreate):
    db_team = Team(name=team.name, department_id=team.department_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def list_cost_centers(db: Session):
    return db.query(CostCenter).all()


def create_cost_center(db: Session, cc: CostCenterCreate):
    db_cc = CostCenter(name=cc.name, code=cc.code)
    db.add(db_cc)
    db.commit()
    db.refresh(db_cc)
    return db_cc

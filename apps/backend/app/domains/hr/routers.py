from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...database import get_db
from .schemas import (
    EmployeeCreate, EmployeeRead,
    SkillCreate, SkillRead,
    CertificationCreate, CertificationRead,
    AttendanceCreate, AttendanceRead,
    LeaveBalanceRead, LeaveRequestCreate
)
from . import services

router = APIRouter()


@router.get("/employees", response_model=list[EmployeeRead])
def list_employees(db: Session = Depends(get_db)):
    return services.list_employees(db)


@router.post("/employees", response_model=EmployeeRead)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return services.create_employee(db, emp)


@router.get("/employees/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = services.get_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@router.get("/skills", response_model=list[SkillRead])
def list_skills(db: Session = Depends(get_db)):
    return services.list_skills(db)


@router.post("/skills", response_model=SkillRead)
def add_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    return services.add_skill(db, skill)


@router.get("/certifications", response_model=list[CertificationRead])
def list_certifications(db: Session = Depends(get_db)):
    return services.list_certifications(db)


@router.post("/certifications", response_model=CertificationRead)
def add_certification(cert: CertificationCreate, db: Session = Depends(get_db)):
    return services.add_certification(db, cert)


@router.get("/availability")
def list_availability(db: Session = Depends(get_db)):
    return services.get_availability(db)


@router.patch("/availability/{employee_id}")
def update_availability(employee_id: int, status: str, db: Session = Depends(get_db)):
    emp = services.update_availability(db, employee_id, status)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"status": "updated", "employee_id": employee_id, "availability": status}


@router.post("/attendance/check-in", response_model=AttendanceRead)
def check_in(att: AttendanceCreate, db: Session = Depends(get_db)):
    return services.check_in(db, att)


@router.post("/attendance/check-out/{employee_id}", response_model=AttendanceRead)
def check_out(employee_id: int, db: Session = Depends(get_db)):
    att = services.check_out(db, employee_id)
    if not att:
        raise HTTPException(status_code=404, detail="Open attendance check-in session not found")
    return att


@router.get("/attendance", response_model=list[AttendanceRead])
def list_attendance(db: Session = Depends(get_db)):
    return services.get_attendance_log(db)


@router.get("/leave-balances", response_model=list[LeaveBalanceRead])
def list_leave_balances(db: Session = Depends(get_db)):
    return services.get_leave_balance(db)


@router.post("/leave-requests")
def create_leave_request(req: LeaveRequestCreate, db: Session = Depends(get_db)):
    return services.request_leave(db, req)

from sqlalchemy.orm import Session
from datetime import datetime
from .models import Employee, Skill, Certification, Attendance, LeaveBalance
from .schemas import (
    EmployeeCreate, SkillCreate, CertificationCreate,
    AttendanceCreate, LeaveBalanceCreate, LeaveRequestCreate
)


def list_employees(db: Session):
    return db.query(Employee).all()


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def create_employee(db: Session, emp: EmployeeCreate):
    db_emp = Employee(
        first_name=emp.first_name,
        last_name=emp.last_name,
        email=emp.email,
        department_id=emp.department_id,
        designation=emp.designation,
        photo_url=emp.photo_url,
        status=emp.status
    )
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def update_employee(db: Session, employee_id: int, updates: dict):
    db_emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_emp:
        return None
    for k, v in updates.items():
        if hasattr(db_emp, k):
            setattr(db_emp, k, v)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def list_skills(db: Session):
    return db.query(Skill).all()


def add_skill(db: Session, skill: SkillCreate):
    db_skill = Skill(employee_id=skill.employee_id, name=skill.name, proficiency=skill.proficiency)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def list_certifications(db: Session):
    return db.query(Certification).all()


def add_certification(db: Session, cert: CertificationCreate):
    db_cert = Certification(
        employee_id=cert.employee_id,
        name=cert.name,
        issued_date=cert.issued_date,
        expiry_date=cert.expiry_date
    )
    db.add(db_cert)
    db.commit()
    db.refresh(db_cert)
    return db_cert


def get_availability(db: Session):
    return db.query(Employee.id, Employee.first_name, Employee.last_name, Employee.status).all()


def update_availability(db: Session, employee_id: int, status: str):
    db_emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_emp:
        db_emp.status = status
        db.commit()
        db.refresh(db_emp)
    return db_emp


def check_in(db: Session, att: AttendanceCreate):
    db_att = Attendance(
        employee_id=att.employee_id,
        check_in=att.check_in or datetime.utcnow(),
        overtime_hours=att.overtime_hours
    )
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att


def check_out(db: Session, employee_id: int):
    # Find the latest open attendance (check_out is None)
    db_att = db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.check_out == None
    ).order_by(Attendance.check_in.desc()).first()
    if db_att:
        db_att.check_out = datetime.utcnow()
        db.commit()
        db.refresh(db_att)
    return db_att


def get_attendance_log(db: Session):
    return db.query(Attendance).all()


def get_leave_balance(db: Session):
    return db.query(LeaveBalance).all()


def request_leave(db: Session, req: LeaveRequestCreate):
    # Leave workflow logic stub, register balance usage
    balance = db.query(LeaveBalance).filter(
        LeaveBalance.employee_id == req.employee_id,
        LeaveBalance.leave_type == req.leave_type
    ).first()
    if not balance:
        balance = LeaveBalance(
            employee_id=req.employee_id,
            leave_type=req.leave_type,
            total_days=15.0,
            used_days=0.0
        )
        db.add(balance)
        db.commit()
        db.refresh(balance)

    # Simple workflow: approve automatically and update availability status
    days = (req.end_date - req.start_date).days + 1
    balance.used_days += days
    db_emp = db.query(Employee).filter(Employee.id == req.employee_id).first()
    if db_emp:
        db_emp.status = "Leave"
    db.commit()
    return balance

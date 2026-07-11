"""HR domain Pydantic schemas."""
from pydantic import BaseModel
from datetime import date, datetime


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    department_id: int | None = None
    designation: str | None = None
    photo_url: str | None = None
    status: str | None = "Available"


class EmployeeRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department_id: int | None = None
    designation: str | None = None
    photo_url: str | None = None
    status: str | None = None

    class Config:
        from_attributes = True


class SkillCreate(BaseModel):
    employee_id: int
    name: str
    proficiency: str | None = None


class SkillRead(BaseModel):
    id: int
    employee_id: int
    name: str
    proficiency: str | None = None

    class Config:
        from_attributes = True


class CertificationCreate(BaseModel):
    employee_id: int
    name: str
    issued_date: date | None = None
    expiry_date: date | None = None


class CertificationRead(BaseModel):
    id: int
    employee_id: int
    name: str
    issued_date: date | None = None
    expiry_date: date | None = None

    class Config:
        from_attributes = True


class AttendanceCreate(BaseModel):
    employee_id: int
    check_in: datetime | None = None
    check_out: datetime | None = None
    overtime_hours: float | None = 0.0


class AttendanceRead(BaseModel):
    id: int
    employee_id: int
    check_in: datetime | None = None
    check_out: datetime | None = None
    overtime_hours: float

    class Config:
        from_attributes = True


class LeaveBalanceCreate(BaseModel):
    employee_id: int
    leave_type: str
    total_days: float
    used_days: float | None = 0.0


class LeaveBalanceRead(BaseModel):
    id: int
    employee_id: int
    leave_type: str
    total_days: float
    used_days: float

    class Config:
        from_attributes = True


class LeaveRequestCreate(BaseModel):
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    reason: str | None = None

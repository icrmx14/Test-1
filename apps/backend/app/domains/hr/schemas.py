"""HR domain Pydantic schemas."""
from pydantic import BaseModel
from datetime import date, datetime


class EmployeeRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    designation: str | None = None
    status: str | None = None
    class Config:
        from_attributes = True

class SkillRead(BaseModel):
    id: int
    employee_id: int
    name: str
    proficiency: str | None = None
    class Config:
        from_attributes = True

class AttendanceRead(BaseModel):
    id: int
    employee_id: int
    check_in: datetime | None = None
    check_out: datetime | None = None
    overtime_hours: float
    class Config:
        from_attributes = True

class LeaveBalanceRead(BaseModel):
    id: int
    employee_id: int
    leave_type: str
    total_days: float
    used_days: float
    class Config:
        from_attributes = True

"""HR domain models: Employee, Skill, Certification, Calendar, Availability, Attendance, LeaveBalance."""
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Float, Enum as SAEnum
from ...database import Base
import enum


class AvailabilityStatus(str, enum.Enum):
    AVAILABLE = "Available"
    BUSY = "Busy"
    MEETING = "Meeting"
    WFH = "WFH"
    LEAVE = "Leave"
    SICK = "Sick"
    CLIENT_VISIT = "Client Visit"
    TRAVEL = "Travel"


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    designation = Column(String, nullable=True)
    photo_url = Column(String, nullable=True)
    status = Column(String, default=AvailabilityStatus.AVAILABLE)


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    name = Column(String, nullable=False)
    proficiency = Column(String, nullable=True)


class Certification(Base):
    __tablename__ = "certifications"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    name = Column(String, nullable=False)
    issued_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)


class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    check_in = Column(DateTime, nullable=True)
    check_out = Column(DateTime, nullable=True)
    overtime_hours = Column(Float, default=0.0)


class LeaveBalance(Base):
    __tablename__ = "leave_balances"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    leave_type = Column(String, nullable=False)
    total_days = Column(Float, default=0.0)
    used_days = Column(Float, default=0.0)

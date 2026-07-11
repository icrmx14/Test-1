"""Projects domain Pydantic schemas."""
from pydantic import BaseModel
from datetime import date

class ProjectRead(BaseModel):
    id: int
    name: str
    status: str
    start_date: date | None = None
    end_date: date | None = None
    class Config:
        from_attributes = True

class MilestoneRead(BaseModel):
    id: int
    project_id: int
    title: str
    due_date: date | None = None
    completed: int
    class Config:
        from_attributes = True

class KanbanCardRead(BaseModel):
    id: int
    project_id: int
    title: str
    column: str
    class Config:
        from_attributes = True

class TimesheetRead(BaseModel):
    id: int
    employee_id: int
    project_id: int
    date: date
    hours: float
    billable: int
    class Config:
        from_attributes = True

class WorkloadRead(BaseModel):
    id: int
    employee_id: int
    utilization_pct: float
    capacity_hours: float
    burnout_risk: str
    is_idle: int
    class Config:
        from_attributes = True

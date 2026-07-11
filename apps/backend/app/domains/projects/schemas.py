"""Projects domain Pydantic schemas."""
from pydantic import BaseModel
from datetime import date


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    status: str | None = "Planning"
    start_date: date | None = None
    end_date: date | None = None


class ProjectRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    status: str
    start_date: date | None = None
    end_date: date | None = None

    class Config:
        from_attributes = True


class MilestoneCreate(BaseModel):
    project_id: int
    title: str
    due_date: date | None = None
    completed: int | None = 0


class MilestoneRead(BaseModel):
    id: int
    project_id: int
    title: str
    due_date: date | None = None
    completed: int

    class Config:
        from_attributes = True


class KanbanCardCreate(BaseModel):
    project_id: int
    title: str
    column: str | None = "Backlog"
    assignee_id: int | None = None


class KanbanCardRead(BaseModel):
    id: int
    project_id: int
    title: str
    column: str
    assignee_id: int | None = None

    class Config:
        from_attributes = True


class TimesheetCreate(BaseModel):
    employee_id: int
    project_id: int
    date: date
    hours: float
    billable: int | None = 1


class TimesheetRead(BaseModel):
    id: int
    employee_id: int
    project_id: int
    date: date
    hours: float
    billable: int

    class Config:
        from_attributes = True


class WorkloadCreate(BaseModel):
    employee_id: int
    utilization_pct: float | None = 0.0
    capacity_hours: float | None = 40.0
    burnout_risk: str | None = "Low"
    is_idle: int | None = 0


class WorkloadRead(BaseModel):
    id: int
    employee_id: int
    utilization_pct: float
    capacity_hours: float
    burnout_risk: str
    is_idle: int

    class Config:
        from_attributes = True

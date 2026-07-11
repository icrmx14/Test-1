from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from .schemas import (
    ProjectCreate, ProjectRead,
    MilestoneCreate, MilestoneRead,
    KanbanCardCreate, KanbanCardRead,
    TimesheetCreate, TimesheetRead,
    WorkloadRead
)
from . import services

router = APIRouter()


@router.get("/projects", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return services.list_projects(db)


@router.post("/projects", response_model=ProjectRead)
def create_project(proj: ProjectCreate, db: Session = Depends(get_db)):
    return services.create_project(db, proj)


@router.get("/milestones", response_model=list[MilestoneRead])
def list_milestones(db: Session = Depends(get_db)):
    return services.list_milestones(db)


@router.post("/milestones", response_model=MilestoneRead)
def create_milestone(ms: MilestoneCreate, db: Session = Depends(get_db)):
    return services.create_milestone(db, ms)


@router.get("/kanban", response_model=list[KanbanCardRead])
def list_kanban_cards(db: Session = Depends(get_db)):
    return services.list_kanban_cards(db)


@router.post("/kanban", response_model=KanbanCardRead)
def create_kanban_card(kc: KanbanCardCreate, db: Session = Depends(get_db)):
    return services.create_kanban_card(db, kc)


@router.patch("/kanban/{card_id}", response_model=KanbanCardRead)
def move_card(card_id: int, column: str, db: Session = Depends(get_db)):
    kc = services.move_kanban_card(db, card_id, column)
    if not kc:
        raise HTTPException(status_code=404, detail="Kanban card not found")
    return kc


@router.get("/timesheets", response_model=list[TimesheetRead])
def list_timesheets(db: Session = Depends(get_db)):
    return services.list_timesheets(db)


@router.post("/timesheets", response_model=TimesheetRead)
def log_timesheet(ts: TimesheetCreate, db: Session = Depends(get_db)):
    return services.log_timesheet(db, ts)


@router.get("/billable-hours", response_model=list[TimesheetRead])
def get_billable_hours(db: Session = Depends(get_db)):
    return services.get_billable_hours(db)


@router.get("/workload", response_model=list[WorkloadRead])
def get_workload(db: Session = Depends(get_db)):
    return services.get_workload(db)

from sqlalchemy.orm import Session
from .models import Project, Milestone, KanbanCard, Timesheet, WorkloadEntry
from .schemas import (
    ProjectCreate, MilestoneCreate, KanbanCardCreate,
    TimesheetCreate, WorkloadCreate
)


def list_projects(db: Session):
    return db.query(Project).all()


def create_project(db: Session, proj: ProjectCreate):
    db_proj = Project(
        name=proj.name,
        description=proj.description,
        status=proj.status,
        start_date=proj.start_date,
        end_date=proj.end_date
    )
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj


def list_milestones(db: Session):
    return db.query(Milestone).all()


def create_milestone(db: Session, ms: MilestoneCreate):
    db_ms = Milestone(
        project_id=ms.project_id,
        title=ms.title,
        due_date=ms.due_date,
        completed=ms.completed
    )
    db.add(db_ms)
    db.commit()
    db.refresh(db_ms)
    return db_ms


def list_kanban_cards(db: Session):
    return db.query(KanbanCard).all()


def create_kanban_card(db: Session, kc: KanbanCardCreate):
    db_kc = KanbanCard(
        project_id=kc.project_id,
        title=kc.title,
        column=kc.column,
        assignee_id=kc.assignee_id
    )
    db.add(db_kc)
    db.commit()
    db.refresh(db_kc)
    return db_kc


def move_kanban_card(db: Session, card_id: int, col: str):
    kc = db.query(KanbanCard).filter(KanbanCard.id == card_id).first()
    if kc:
        kc.column = col
        db.commit()
        db.refresh(kc)
    return kc


def list_timesheets(db: Session):
    return db.query(Timesheet).all()


def log_timesheet(db: Session, ts: TimesheetCreate):
    db_ts = Timesheet(
        employee_id=ts.employee_id,
        project_id=ts.project_id,
        date=ts.date,
        hours=ts.hours,
        billable=ts.billable
    )
    db.add(db_ts)
    db.commit()
    db.refresh(db_ts)
    return db_ts


def get_billable_hours(db: Session):
    return db.query(Timesheet).filter(Timesheet.billable == 1).all()


def get_workload(db: Session):
    # Auto-seed workload table if empty
    entries = db.query(WorkloadEntry).all()
    if not entries:
        from ..hr.models import Employee
        employees = db.query(Employee).all()
        for emp in employees:
            wl = WorkloadEntry(
                employee_id=emp.id,
                utilization_pct=65.0,
                capacity_hours=40.0,
                burnout_risk="Low",
                is_idle=0
            )
            db.add(wl)
        db.commit()
        entries = db.query(WorkloadEntry).all()
    return entries


def detect_burnout(db: Session):
    return db.query(WorkloadEntry).filter(WorkloadEntry.utilization_pct > 90.0).all()


def detect_idle_resources(db: Session):
    return db.query(WorkloadEntry).filter(WorkloadEntry.utilization_pct < 20.0).all()

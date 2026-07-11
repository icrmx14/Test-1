"""Projects domain models: Project, Milestone, KanbanCard, Timesheet, WorkloadEntry."""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from ...database import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="Planning")
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

class Milestone(Base):
    __tablename__ = "milestones"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    title = Column(String, nullable=False)
    due_date = Column(Date, nullable=True)
    completed = Column(Integer, default=0)

class KanbanCard(Base):
    __tablename__ = "kanban_cards"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    title = Column(String, nullable=False)
    column = Column(String, default="Backlog")
    assignee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)

class Timesheet(Base):
    __tablename__ = "timesheets"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    date = Column(Date, nullable=False)
    hours = Column(Float, default=0.0)
    billable = Column(Integer, default=1)

class WorkloadEntry(Base):
    __tablename__ = "workload_entries"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    utilization_pct = Column(Float, default=0.0)
    capacity_hours = Column(Float, default=40.0)
    burnout_risk = Column(String, default="Low")
    is_idle = Column(Integer, default=0)

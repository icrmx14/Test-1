from fastapi import APIRouter

router = APIRouter()

@router.get("/projects")
def list_projects():
    return []

@router.post("/projects")
def create_project():
    return {"detail": "stub"}

@router.get("/milestones")
def list_milestones():
    return []

@router.post("/milestones")
def create_milestone():
    return {"detail": "stub"}

@router.get("/kanban")
def list_kanban_cards():
    return []

@router.patch("/kanban/{card_id}")
def move_card(card_id: int):
    return {"detail": "stub"}

@router.get("/timesheets")
def list_timesheets():
    return []

@router.post("/timesheets")
def log_timesheet():
    return {"detail": "stub"}

@router.get("/billable-hours")
def get_billable_hours():
    return []

@router.get("/workload")
def get_workload():
    return []

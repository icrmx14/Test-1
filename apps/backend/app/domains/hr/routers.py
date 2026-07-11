from fastapi import APIRouter

router = APIRouter()

@router.get("/employees")
def list_employees():
    return []

@router.post("/employees")
def create_employee():
    return {"detail": "stub"}

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {"detail": "stub"}

@router.get("/skills")
def list_skills():
    return []

@router.get("/certifications")
def list_certifications():
    return []

@router.get("/availability")
def list_availability():
    return []

@router.post("/attendance/check-in")
def check_in():
    return {"detail": "stub"}

@router.post("/attendance/check-out")
def check_out():
    return {"detail": "stub"}

@router.get("/attendance")
def list_attendance():
    return []

@router.get("/leave-balances")
def list_leave_balances():
    return []

@router.post("/leave-requests")
def create_leave_request():
    return {"detail": "stub"}

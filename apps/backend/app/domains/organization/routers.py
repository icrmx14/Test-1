from fastapi import APIRouter

router = APIRouter()

@router.get("/companies")
def list_companies():
    return []

@router.post("/companies")
def create_company():
    return {"detail": "stub"}

@router.get("/branches")
def list_branches():
    return []

@router.get("/departments")
def list_departments():
    return []

@router.get("/teams")
def list_teams():
    return []

@router.get("/cost-centers")
def list_cost_centers():
    return []

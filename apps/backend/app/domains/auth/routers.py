from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
def register():
    return {"detail": "stub"}


@router.post("/login")
def login():
    return {"detail": "stub"}


@router.get("/roles")
def list_roles():
    return []

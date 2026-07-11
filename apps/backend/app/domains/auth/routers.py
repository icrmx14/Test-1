from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...database import get_db
from .schemas import UserCreate, UserRead, RoleRead
from . import services

router = APIRouter()


@router.post("/register", response_model=UserRead)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        return services.register_user(db, user_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login")
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    res = services.authenticate_user(db, user_data.email, user_data.password)
    if not res:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    return res


@router.get("/roles", response_model=list[RoleRead])
def list_roles(db: Session = Depends(get_db)):
    return services.list_roles(db)

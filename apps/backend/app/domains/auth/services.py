from sqlalchemy.orm import Session
from .models import User, Role
from ...core.security import hash_password, verify_password, create_access_token
from .schemas import UserCreate


def register_user(db: Session, user_data: UserCreate) -> User:
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise ValueError("User with this email already exists")

    hashed = hash_password(user_data.password)
    user = User(email=user_data.email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, plain_pass: str) -> dict | None:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(plain_pass, user.hashed_password):
        return None
    token = create_access_token({"sub": str(user.id), "email": user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": user.id, "email": user.email}
    }


def list_roles(db: Session):
    roles = db.query(Role).all()
    if not roles:
        std_roles = ["Admin", "HR", "Sales", "Procurement", "Operations", "Finance", "Manager", "Employee"]
        for name in std_roles:
            role = Role(name=name, description=f"Standard {name} role")
            db.add(role)
        db.commit()
        roles = db.query(Role).all()
    return roles

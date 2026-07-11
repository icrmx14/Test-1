"""Auth domain Pydantic schemas."""
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserRead(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class RoleRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True

from datetime import date
from pydantic import BaseModel, EmailStr
from enum import Enum
from fastapi import Form


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str

    # is_active: bool = False
    # role: Roles = "user"

    class Config:
        orm_mode = True


class Roles(Enum):
    user = "user"
    admin = "admin"


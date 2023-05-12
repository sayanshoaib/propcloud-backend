from beanie import Document
from pydantic import EmailStr
from typing import Optional, List
from datetime import datetime
from app.models.enums.role import Role


class User(Document):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str]
    disabled: Optional[bool]
    roles: List[Role]
    created_at: datetime
    updated_at: datetime

    class Collection:
        name = "users"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "shoaib-hasan18",
                "email": "shoaib@gmail.com",
                "password": "secretpassword",
                "full_name": "Shoaib Hasan",
                "disabled": False,
                "roles": ["customer", "agent"],
                "created_at": "2008-09-15T15:53:00+05:00",
                "updated_at": "2008-09-15T15:53:00+05:00"
            }
        }


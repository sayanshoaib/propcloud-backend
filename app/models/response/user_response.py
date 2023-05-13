from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from app.models.enums.role import Role


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str]
    disabled: Optional[bool]
    roles: List[Role]
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "shoaib-hasan18",
                "email": "shoaib@gmail.com",
                "full_name": "Shoaib Hasan",
                "roles": ["admin", "agent"],
                "disabled": False
            }
        }

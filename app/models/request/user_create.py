from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from app.models.enums.role import Role


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=5, max_length=254)
    password: str = Field(..., max_length=8)
    full_name: Optional[str] = Field(None, min_length=3, max_length=50)
    disabled: Optional[bool] = Field(False)
    roles: List[Role]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "shoaib-hasan18",
                "email": "shoaib@gmail.com",
                "password": "secretpassword",
                "full_name": "Shoaib Hasan",
                "roles": ["admin", "agent"],
                "disabled": False
            }
        }

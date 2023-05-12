from typing import List, Optional
from pydantic import BaseModel, Field


class Unit(BaseModel):
    unit_number: str = Field(..., min_length=1, max_length=50)
    square_feet: Optional[int] = Field(None, ge=0)
    bedrooms: Optional[int] = Field(None, ge=0)
    bathrooms: Optional[int] = Field(None, ge=0)
    monthly_rent: Optional[float] = Field(None, ge=0)
    leased: Optional[bool] = Field(False)
    property_id: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "unit_number": "A101",
                "square_feet": 800,
                "bedrooms": 1,
                "bathrooms": 1,
                "monthly_rent": 1500.0,
                "leased": False,
                "property_id": "property_id"
            }
        }

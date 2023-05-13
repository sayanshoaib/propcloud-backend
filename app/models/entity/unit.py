from beanie import Document
from typing import List, Optional
from datetime import datetime


class Unit(Document):
    unit_number: str
    square_feet: Optional[int]
    bedrooms: Optional[int]
    bathrooms: Optional[int]
    monthly_rent: Optional[float]
    leased: Optional[bool]
    property_id: str
    created_at: datetime
    updated_at: datetime

    class Collection:
        name = "units"

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
                "property_id": "property_id",
                "created_at": "2008-09-15T15:53:00+05:00",
                "updated_at": "2008-09-15T15:53:00+05:00",
            }
        }

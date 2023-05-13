from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Location(BaseModel):
    address_line_1: str
    address_line_2: Optional[str]
    city: str
    state: str
    zip_code: str
    country: str
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime

    class Collection:
        name = "locations"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "address_line_1": "123 Main St",
                "address_line_2": "Apt 2B",
                "city": "San Francisco",
                "state": "CA",
                "zip_code": "94111",
                "country": "Iceland",
                "latitude": 37.7749,
                "longitude": -122.4194,
                "created_at": "2008-09-15T15:53:00+05:00",
                "updated_at": "2008-09-15T15:53:00+05:00"
            }
        }

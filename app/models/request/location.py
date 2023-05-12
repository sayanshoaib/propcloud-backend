from typing import Optional
from pydantic import BaseModel, Field


class Location(BaseModel):
    address_line_1: str = Field(..., min_length=1, max_length=100)
    address_line_2: Optional[str] = Field(None, max_length=100)
    city: str = Field(..., min_length=1, max_length=50)
    state: str = Field(..., min_length=2, max_length=2)
    zip_code: str = Field(..., min_length=5, max_length=10)
    country: str = Field(..., min_length=3, max_length=100)
    latitude: Optional[float] = None
    longitude: Optional[float] = None

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
                "longitude": -122.4194
            }
        }
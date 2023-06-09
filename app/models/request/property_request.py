from typing import Optional, List
from pydantic import BaseModel, Field
from app.models.request.unit_request import UnitRequest
from app.models.request.location_request import LocationRequest


class PropertyRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    units: List[UnitRequest] = Field(None, ge=0)
    price: Optional[float] = Field(None, ge=0)
    location: LocationRequest
    owner_id: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Beautiful House",
                "description": "A beautiful house with a view",
                "units": [
                    {
                        "unit_number": "A101",
                        "square_feet": 800,
                        "bedrooms": 1,
                        "bathrooms": 1,
                        "monthly_rent": 1500.0,
                        "leased": False,
                        "property_id": "property_id"
                    },
                    {
                        "unit_number": "A102",
                        "square_feet": 800,
                        "bedrooms": 1,
                        "bathrooms": 1,
                        "monthly_rent": 1500.0,
                        "leased": False,
                        "property_id": "property_id"
                    }
                ],
                "price": 250000.0,
                "location": {
                    "address_line_1": "123 Main St",
                    "address_line_2": "Apt 2B",
                    "city": "San Francisco",
                    "state": "CA",
                    "zip_code": "94111",
                    "country": "Iceland",
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
                "owner_id": "user_id"
            }
        }

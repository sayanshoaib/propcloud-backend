from beanie import Document
from typing import Optional, List
from datetime import datetime
from app.models.request.unit import Unit
from app.models.request.location import Location


class Property(Document):
    name: str
    description: Optional[str]
    units: List[Unit]
    price: Optional[float]
    location: Location
    owner_id: str
    created_at: datetime
    updated_at: datetime

    class Collection:
        name = "properties"

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
                        "property_id": "property_id",
                        "created_at": "2008-09-15T15:53:00+05:00",
                        "updated_at": "2008-09-15T15:53:00+05:00"
                    },
                    {
                        "unit_number": "A102",
                        "square_feet": 800,
                        "bedrooms": 1,
                        "bathrooms": 1,
                        "monthly_rent": 1500.0,
                        "leased": False,
                        "property_id": "property_id",
                        "created_at": "2008-09-15T15:53:00+05:00",
                        "updated_at": "2008-09-15T15:53:00+05:00"
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
                    "longitude": -122.4194,
                    "created_at": "2008-09-15T15:53:00+05:00",
                    "updated_at": "2008-09-15T15:53:00+05:00"
                },
                "owner_id": "user_id",
                "created_at": "2008-09-15T15:53:00+05:00",
                "updated_at": "2008-09-15T15:53:00+05:00"
            }
        }

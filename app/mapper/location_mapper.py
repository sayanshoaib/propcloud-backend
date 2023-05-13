from app.models.request.location_request import LocationRequest
from app.models.entity.location import Location


def map_to_location(location_request: LocationRequest) -> Location:
    location_request_dict = location_request.dict()
    return Location(**location_request_dict)
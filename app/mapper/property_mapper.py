from app.models.request.property_request import PropertyRequest
from app.models.entity.property import Property


def map_to_property(property_request: PropertyRequest) -> Property:
    property_dict = property_request.dict()
    return Property(**property_dict)

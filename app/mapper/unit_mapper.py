from app.models.request.unit_request import UnitRequest
from app.models.entity.unit import Unit


def map_to_unit(unit_request: UnitRequest) -> Unit:
    unit_dict = unit_request.dict()
    return Unit(**unit_dict)

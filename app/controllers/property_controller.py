from typing import List

from fastapi import Depends, HTTPException

from app.models.entity.property import Property
from app.models.request.property_request import PropertyRequest
from app.service.property_service import PropertyService
from app.service.unit_service import UnitService
from app.service.location_service import LocationService


from fastapi_utils.cbv import cbv

from app.controllers.base_controller import BaseController, router


@cbv(router)
class PropertyController(BaseController):
    def __init__(self,
                 property_service: PropertyService = Depends(),
                 unit_service: UnitService = Depends(),
                 location_service: LocationService = Depends()
                 ):
        self.property_service = property_service
        self.unit_service = unit_service
        self.location_service = location_service

    @router.post("/properties", response_model=Property, status_code=201)
    async def create_new_property(self, property_create: PropertyRequest) -> Property:
        unit = await self.unit_service.get_unit_by_id(property_create.unit_id)
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
        location = await self.location_service.get_location_by_id(property_create.location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")

        prop = await self.property_service.create_property(property_create)
        return prop

    @router.get("/properties/{property_id}/", response_model=Property)
    async def read_property_by_id(self, property_id: str) -> Property:
        prop = await self.property_service.get_property_by_id(property_id)
        if not prop:
            raise HTTPException(status_code=404, detail="Property not found")
        return prop

    @router.get("/properties", response_model=List[Property])
    async def read_all_properties(self) -> List[Property]:
        properties = await self.property_service.get_all_properties()
        return properties

    @router.put("/properties/{property_id}/", response_model=Property)
    async def update_property(self, property_id: str, property_update: PropertyRequest) -> Property:
        prop = await self.property_service.get_property_by_id(property_id=property_id)
        if not prop:
            raise HTTPException(status_code=404, detail="Property not found")

        unit = await self.unit_service.get_unit_by_id(property_update.unit_id)
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
        location = await self.location_service.get_location_by_id(property_update.location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")

        updated_property = await self.property_service.update_property(property_id, property_update)
        return updated_property

    @router.delete("/properties/{property_id}/", response_model=bool)
    async def delete_property(self, property_id: str) -> bool:
        prop = await self.property_service.get_property_by_id(property_id=property_id)
        if not prop:
            raise HTTPException(status_code=404, detail="Property not found")
        deleted = await self.property_service.delete_property(property_id=property_id)
        return deleted

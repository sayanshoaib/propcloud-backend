from typing import List

from fastapi import Depends, HTTPException

from app.models.request.location_request import LocationRequest
from app.service.location_service import LocationService
from app.models.entity.location import Location
from fastapi_utils.cbv import cbv

from app.controllers.base_controller import BaseController, router


@cbv(router)
class LocationController(BaseController):
    def __init__(self, location_service: LocationService = Depends()):
        self.location_service = location_service

    @router.post("/locations", response_model=Location, status_code=201)
    async def create_new_location(self, location_create: LocationRequest) -> Location:
        location = await self.location_service.create_location(location_create=location_create)
        return location

    @router.get("/locations/{location_id}/", response_model=Location)
    async def read_location_by_id(self, location_id: str) -> Location:
        location = await self.location_service.get_location_by_id(location_id=location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        return location

    @router.get("/locations", response_model=List[Location])
    async def read_all_locations(self) -> List[Location]:
        locations = await self.location_service.get_all_locations()
        return locations

    @router.put("/locations/{location_id}/", response_model=Location)
    async def update_location(self, location_id: str, location_update: LocationRequest) -> Location:
        location = await self.location_service.get_location_by_id(location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        updated_location = await self.location_service.update_location(location_id, location_update)
        return updated_location

    @router.delete("/{location_id}/", response_model=bool)
    async def delete_location(self, location_id: str) -> bool:
        location = await self.location_service.get_location_by_id(location_id)
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        deleted = await self.location_service.delete_location(location_id)
        return deleted

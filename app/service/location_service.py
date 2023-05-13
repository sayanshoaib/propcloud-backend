from typing import List, Optional
from app.repository.location_repository import LocationRepository
from app.mapper.location_mapper import *


class LocationService:
    def __init__(self, location_repo: LocationRepository):
        self.location_repo = location_repo

    async def create_location(self, location_create: LocationRequest) -> Location:
        location = map_to_location(location_create)
        return await self.location_repo.create_location(location)

    async def get_location_by_id(self, location_id: str) -> Optional[Location]:
        return await self.location_repo.get_location_by_id(location_id)

    async def update_location(self, location_id: str, location_update: LocationRequest) -> Location:
        location = map_to_location(location_update)
        return await self.location_repo.update_location(location_id, location)

    async def delete_location(self, location_id: str) -> Optional[bool]:
        return await self.location_repo.delete_location(location_id)

    async def get_all_locations(self) -> List[Location]:
        return await self.location_repo.get_all_locations()

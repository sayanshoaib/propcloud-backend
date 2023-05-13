from typing import List, Optional

from app.repository.property_repository import PropertyRepository
from app.mapper.property_mapper import *


class PropertyService:
    def __init__(self, property_repository: PropertyRepository):
        self.property_repository = property_repository

    async def create_property(self, property_create: PropertyRequest) -> Property:
        prop_entity = map_to_property(property_create)
        created_property = await self.property_repository.create_property(prop_entity)
        return created_property

    async def get_property_by_id(self, property_id: str) -> Property:
        property_obj = await self.property_repository.get_property_by_id(property_id)
        return property_obj

    async def get_all_properties(self) -> List[Property]:
        properties = await self.property_repository.get_all_properties()
        return properties

    async def update_property(self, property_id: str, property_update: PropertyRequest) -> Property:
        prop_entity = map_to_property(property_update)
        updated_property = await self.property_repository.update_property(property_id, prop_entity)
        return updated_property

    async def delete_property(self, property_id: str) -> Optional[bool]:
        return await self.property_repository.delete_property(property_id)

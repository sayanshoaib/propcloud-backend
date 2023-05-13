from typing import List, Optional

from app.repository.unit_repository import UnitRepository
from app.mapper.unit_mapper import *


class UnitService:
    def __init__(self, unit_repo: UnitRepository):
        self.unit_repo = unit_repo

    async def create_unit(self, unit_create: UnitRequest) -> Unit:
        unit = map_to_unit(unit_create)
        return await self.unit_repo.create_unit(unit)

    async def get_unit_by_id(self, unit_id: str) -> Optional[Unit]:
        return await self.unit_repo.get_unit_by_id(unit_id)

    async def update_unit(self, unit_id: str, unit_update: UnitRequest) -> Unit:
        unit = map_to_unit(unit_update)
        return await self.unit_repo.update_unit(unit_id, unit)

    async def delete_unit(self, unit_id: str) -> Optional[bool]:
        return await self.unit_repo.delete_unit(unit_id)

    async def get_all_units(self) -> List[Unit]:
        return await self.unit_repo.get_all_units()

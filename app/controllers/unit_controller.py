from typing import List

from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv

from app.controllers.base_controller import BaseController, router
from app.models.request.unit_request import UnitRequest
from app.models.entity.unit import Unit
from app.service.unit_service import UnitService


@cbv(router)
class UnitController(BaseController):
    def __init__(self, unit_service: UnitService = Depends()):
        self.unit_service = unit_service

    @router.post("/units", response_model=Unit, status_code=201)
    async def create_new_unit(self, unit_create: UnitRequest) -> Unit:
        unit = await self.unit_service.create_unit(unit_create)
        return unit

    @router.get("/units/{unit_id}/", response_model=Unit)
    async def read_unit_by_id(self, unit_id: str) -> Unit:
        unit = await self.unit_service.get_unit_by_id(unit_id)
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
        return unit

    @router.get("/units", response_model=List[Unit])
    async def read_all_units(self) -> List[Unit]:
        units = await self.unit_service.get_all_units()
        return units

    @router.put("/units/{unit_id}/", response_model=Unit)
    async def update_unit(self, unit_id: str, unit_update: UnitRequest) -> Unit:
        unit = await self.unit_service.get_unit_by_id(unit_id)
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
        updated_unit = await self.unit_service.update_unit(unit_id=unit_id, unit_update=unit_update)
        return updated_unit

    @router.delete("/units/{unit_id}/", response_model=bool)
    async def delete_unit(self, unit_id: str) -> bool:
        unit = await self.unit_service.get_unit_by_id(unit_id)
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
        deleted = await self.unit_service.delete_unit(unit_id)
        return deleted

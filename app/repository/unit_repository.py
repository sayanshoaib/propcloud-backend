from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from typing import List, Optional

from app.models.entity.unit import Unit


class UnitRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def create_unit(self, unit: Unit) -> Unit:
        unit_dict = unit.dict()
        result: InsertOneResult = await self.collection.insert_one(unit_dict)
        unit_id = str(result.inserted_id)
        return Unit(id=unit_id, **unit_dict)

    async def get_unit_by_id(self, unit_id: str) -> Optional[Unit]:
        unit_dict = await self.collection.find_one({"_id": ObjectId(unit_id)})
        if unit_dict:
            unit_dict["id"] = str(unit_dict["_id"])
            return Unit(**unit_dict)
        return None

    async def update_unit(self, unit_id: str, unit: Unit) -> Optional[Unit]:
        unit_dict = unit.dict(exclude_unset=True)
        result: UpdateResult = await self.collection.update_one(
            {"_id": ObjectId(unit_id)}, {"$set": unit_dict}
        )
        if result.modified_count == 1:
            updated_unit_dict = await self.collection.find_one({"_id": ObjectId(unit_id)})
            updated_unit_dict["id"] = str(updated_unit_dict["_id"])
            return Unit(**updated_unit_dict)
        return None

    async def delete_unit(self, unit_id: str) -> Optional[DeleteResult]:
        result: DeleteResult = await self.collection.delete_one({"_id": ObjectId(unit_id)})
        if result.deleted_count == 1:
            return result
        return None

    async def get_all_units(self) -> List[Unit]:
        cursor = self.collection.find()
        units = []
        async for unit_dict in cursor:
            unit_dict["id"] = str(unit_dict["_id"])
            units.append(Unit(**unit_dict))
        return units

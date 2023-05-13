from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from typing import List, Optional

from app.models.entity.property import Property
from app.repository.unit_repository import UnitRepository
from app.repository.location_repository import LocationRepository


class PropertyRepository:
    def __init__(self, collection: Collection, unit_repo: UnitRepository, location_repo: LocationRepository):
        self.collection = collection
        self.unit_repo = unit_repo
        self.location_repo = location_repo

    async def create_property(self, property: Property) -> Property:
        unit = await self.unit_repo.get_unit_by_id(property.unit_id)
        location = await self.location_repo.get_location_by_id(property.location_id)
        if not unit or not location:
            return None
        property_dict = property.dict()
        property_dict["unit"] = unit.dict()
        property_dict["location"] = location.dict()
        result: InsertOneResult = await self.collection.insert_one(property_dict)
        property_id = str(result.inserted_id)
        return Property(id=property_id, **property_dict)

    async def get_property_by_id(self, property_id: str) -> Optional[Property]:
        property_dict = await self.collection.find_one({"_id": ObjectId(property_id)})
        if property_dict:
            property_dict["id"] = str(property_dict["_id"])
            unit_dict = property_dict.pop("unit")
            location_dict = property_dict.pop("location")
            unit = await self.unit_repo.get_unit_by_id(unit_dict["id"])
            location = await self.location_repo.get_location_by_id(location_dict["id"])
            property_dict["unit"] = unit.dict()
            property_dict["location"] = location.dict()
            return Property(**property_dict)
        return None

    async def update_property(self, property_id: str, property: Property) -> Optional[Property]:
        property_dict = property.dict(exclude_unset=True)
        unit = await self.unit_repo.get_unit_by_id(property.unit_id) if property.unit_id else None
        location = await self.location_repo.get_location_by_id(property.location_id) if property.location_id else None
        if not unit or not location:
            return None
        property_dict["unit"] = unit.dict()
        property_dict["location"] = location.dict()
        result: UpdateResult = await self.collection.update_one(
            {"_id": ObjectId(property_id)}, {"$set": property_dict}
        )
        if result.modified_count == 1:
            updated_property_dict = await self.collection.find_one({"_id": ObjectId(property_id)})
            updated_property_dict["id"] = str(updated_property_dict["_id"])
            unit_dict = updated_property_dict.pop("unit")
            location_dict = updated_property_dict.pop("location")
            unit = await self.unit_repo.get_unit_by_id(unit_dict["id"])
            location = await self.location_repo.get_location_by_id(location_dict["id"])
            updated_property_dict["unit"] = unit.dict()
            updated_property_dict["location"] = location.dict()
            return Property(**updated_property_dict)
        return None

    async def delete_property(self, property_id: str) -> Optional[DeleteResult]:
        result: DeleteResult = await self.collection.delete_one({"_id": ObjectId(property_id)})
        if result.deleted_count == 1:
            return result
        return None

    async def get_all_properties(self) -> List[Property]:
        cursor = self.collection.find()
        properties = []
        async for property_dict in cursor:
            property_dict["id"] = str(property_dict["_id"])
            unit_dict = property_dict.pop("unit")
            location_dict = property_dict.pop("location")
            unit = await self.unit_repo.get_unit_by_id(unit_dict["id"])
            location = await self.location_repo.get_location_by_id(location_dict["id"])
            property_dict["unit"] = unit.dict()
            property_dict["location"] = location.dict()
            properties.append(Property(**property_dict))
        return properties

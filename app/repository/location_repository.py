from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from typing import List, Optional

from app.models.entity.location import Location


class LocationRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def create_location(self, location: Location) -> Location:
        location_dict = location.dict()
        result: InsertOneResult = await self.collection.insert_one(location_dict)
        location_id = str(result.inserted_id)
        return Location(id=location_id, **location_dict)

    async def get_location_by_id(self, location_id: str) -> Optional[Location]:
        location_dict = await self.collection.find_one({"_id": ObjectId(location_id)})
        if location_dict:
            location_dict["id"] = str(location_dict["_id"])
            return Location(**location_dict)
        return None

    async def update_location(self, location_id: str, location: Location) -> Optional[Location]:
        location_dict = location.dict(exclude_unset=True)
        result: UpdateResult = await self.collection.update_one(
            {"_id": ObjectId(location_id)}, {"$set": location_dict}
        )
        if result.modified_count == 1:
            updated_location_dict = await self.collection.find_one({"_id": ObjectId(location_id)})
            updated_location_dict["id"] = str(updated_location_dict["_id"])
            return Location(**updated_location_dict)
        return None

    async def delete_location(self, location_id: str) -> Optional[DeleteResult]:
        result: DeleteResult = await self.collection.delete_one({"_id": ObjectId(location_id)})
        if result.deleted_count == 1:
            return result
        return None

    async def get_all_locations(self) -> List[Location]:
        cursor = self.collection.find()
        locations = []
        async for location_dict in cursor:
            location_dict["id"] = str(location_dict["_id"])
            locations.append(Location(**location_dict))
        return locations

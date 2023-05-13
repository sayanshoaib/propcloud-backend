from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult
from typing import List, Optional
from pydantic import EmailStr
from app.models.entity.user import User


class UserRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def create_user(self, user: User) -> User:
        user_dict = user.dict()
        result: InsertOneResult = await self.collection.insert_one(user_dict)
        user_id = str(result.inserted_id)
        return User(id=user_id, **user_dict)

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        user_dict = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user_dict:
            user_dict["id"] = str(user_dict["_id"])
            return User(**user_dict)
        return None

    async def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        user_dict = await self.collection.find_one({"email": email})
        if user_dict:
            user_dict["id"] = str(user_dict["_id"])
            return User(**user_dict)
        return None

    async def update_user(self, user_id: str, user: User) -> Optional[User]:
        user_dict = user.dict(exclude_unset=True)
        result: UpdateResult = await self.collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": user_dict}
        )
        if result.modified_count == 1:
            updated_user_dict = await self.collection.find_one({"_id": ObjectId(user_id)})
            updated_user_dict["id"] = str(updated_user_dict["_id"])
            return User(**updated_user_dict)
        return None

    async def delete_user(self, user_id: str) -> Optional[DeleteResult]:
        result: DeleteResult = await self.collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 1:
            return result
        return None

    async def get_all_users(self) -> List[User]:
        cursor = self.collection.find()
        users = []
        async for user_dict in cursor:
            user_dict["id"] = str(user_dict["_id"])
            users.append(User(**user_dict))
        return users

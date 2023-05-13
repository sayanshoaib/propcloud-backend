from typing import List, Optional
from pydantic import EmailStr
from datetime import datetime
from app.repository.user_repository import UserRepository
from app.mapper.user_mapper import *


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_create: UserRequest) -> UserResponse:
        user = map_to_user(user_create)
        current_timestamp = int(datetime.now().timestamp())
        user.created_at = current_timestamp
        user_entity = await self.user_repo.create_user(user)
        return map_to_user_response(user_entity)

    async def get_user_by_email(self, email: EmailStr) -> Optional[UserResponse]:
        user_entity = await self.user_repo.get_user_by_email(email)
        return map_to_user_response(user_entity)

    async def get_user_by_id(self, user_id: str) -> Optional[UserResponse]:
        user_entity = await self.user_repo.get_user_by_id(user_id)
        return map_to_user_response(user_entity)

    # async def authenticate_user(self, email: EmailStr, password: str) -> Optional[UserResponse]:
    #     user = await self.get_user_by_email(email)
    #     if not user:
    #         return None
    #     if not user.verify_password(password):
    #         return None
    #     return user

    async def update_user(self, user_id: str, user_update: UserRequest) -> UserResponse:
        new_user = map_to_user(user_update)
        user_entity = await self.user_repo.update_user(user_id, new_user)
        return map_to_user_response(user_entity)

    async def delete_user(self, user_id: str) -> Optional[bool]:
        return await self.user_repo.delete_user(user_id)

    async def get_all_users(self) -> List[UserResponse]:
        users = await self.user_repo.get_all_users()
        user_res = []

        for i, user in enumerate(users):
            user_response = map_to_user_response(user)
            user_res.append(user_response)

        return user_res

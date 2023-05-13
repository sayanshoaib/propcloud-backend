from typing import List

from fastapi import Depends, HTTPException

from fastapi_utils.cbv import cbv

from app.controllers.base_controller import BaseController, router


from app.models.request.user_request import UserRequest
from app.models.response.user_response import UserResponse
from app.service.user_service import UserService


@cbv(router)
class UserController(BaseController):

    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    @router.post("/users", response_model=UserResponse, status_code=201)
    async def create_new_user(self, user_create: UserRequest) -> UserResponse:
        user = await self.user_service.create_user(user_create=user_create)
        return user

    @router.get("users/{user_id}/", response_model=UserResponse)
    async def read_user_by_id(self, user_id: str) -> UserResponse:
        user = await self.user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @router.get("users/", response_model=List[UserResponse])
    async def read_all_users(self) -> List[UserResponse]:
        users = await self.user_service.get_all_users()
        return users

    @router.put("users/{user_id}/", response_model=UserResponse)
    async def update_user(self, user_id: str, user_update: UserRequest) -> UserResponse:
        user = await self.user_service.get_user_by_id(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        updated_user = await self.user_service.update_user(user_id=user_id, user_update=user_update)
        return updated_user

    @router.delete("users/{user_id}/", response_model=bool)
    async def delete_user(self, user_id: str) -> bool:
        user = await self.user_service.get_user_by_id(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        deleted = await self.user_service.delete_user(user_id=user_id)
        return deleted

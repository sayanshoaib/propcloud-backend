from app.models.request.user_request import UserRequest
from app.models.entity.user import User
from app.models.response.user_response import UserResponse


def map_to_user(user_request: UserRequest) -> User:
    user = user_request.dict()
    return User(**user)


def map_to_user_response(user: User) -> UserResponse:
    user_dict = user.dict()
    return UserResponse(**user_dict)

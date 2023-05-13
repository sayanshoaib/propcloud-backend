from fastapi_utils.inferring_router import InferringRouter
from app.config.database import db_conn
from app.repository.user_repository import UserRepository
from app.service.user_service import UserService
from app.controllers.user_controller import UserController


router: InferringRouter = InferringRouter()
router.prefix = "/api"


class BaseController:
    # you can add dependencies here like this example bellow
    # setting = Depends(get_api_settings)
    # db = Depends(get_db)
    user_repo = UserRepository(db_conn("users"))
    user_service = UserService(user_repo)
    user_controller = UserController(user_service)
    pass

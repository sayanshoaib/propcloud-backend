from fastapi_utils.cbv import cbv
from app.config.database import get_server_info

from app.controllers.base_controller import BaseController, router


@cbv(router)
class StatusController(BaseController):

    @router.get("/version", status_code=200)
    async def root(self):
        return {"app_name": "prop-cloud-backend", "app_version": "V1"}

    @router.get("/status", status_code=200)
    async def health_check(self):
        return {
            "status": "ok",
            "message": "I am alive 😀",
            "server_info": get_server_info()
        }

from app.app_context import app
from app.app_routers import app_routers
from app.logger import get_logger

logger = get_logger(__name__)


@app.on_event("startup")
async def startup():
    logger.info("starting server")


@app.on_event("shutdown")
async def shutdown():
    logger.info("shutting down server")


app.include_router(app_routers)

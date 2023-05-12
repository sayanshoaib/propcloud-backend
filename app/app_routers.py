from fastapi_utils.inferring_router import InferringRouter

from app.controllers.status_controller import router as status_router

app_routers: InferringRouter = InferringRouter()

# Registering app routers
app_routers.include_router(status_router)
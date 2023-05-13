from fastapi_utils.inferring_router import InferringRouter


router: InferringRouter = InferringRouter()
router.prefix = "/api"


class BaseController:
    # add dependencies
    # setting = Depends(get_api_settings)
    # db = Depends(get_db)
    pass

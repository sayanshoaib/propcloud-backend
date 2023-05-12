from fastapi_utils.inferring_router import InferringRouter

router: InferringRouter = InferringRouter()


class BaseController:
    # you can add dependencies here like this example bellow
    # setting = Depends(get_api_settings)
    # db = Depends(get_db)
    pass
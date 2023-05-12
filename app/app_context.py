from fastapi import FastAPI

from app import SERVICE_NAME, VERSION

app = FastAPI(
    title=SERVICE_NAME,
    version=VERSION,
    description=SERVICE_NAME
)
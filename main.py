from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"app_name": "prop-cloud-backend", "app_version": "V1"}


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "I am alive 😀"}

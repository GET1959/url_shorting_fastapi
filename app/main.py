from fastapi import FastAPI
from app.urls.routers import router as urls_router


app = FastAPI()


app.include_router(urls_router)

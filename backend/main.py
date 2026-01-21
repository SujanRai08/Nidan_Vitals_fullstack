from fastapi import FastAPI
from app.controllers.observation_controller import router
from app.config import APP_NAME

app = FastAPI(title=APP_NAME)
app.include_router(router)
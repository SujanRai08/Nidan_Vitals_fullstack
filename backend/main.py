from fastapi import FastAPI
from app.controllers.observation_controller import router
from app.config import APP_NAME
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you'd specify your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import engine, Base
from app.routes import inventory, forecasting

# Automatically creates tables in your database on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach modules to router tree
app.include_router(inventory.router, prefix=settings.API_V1_STR)
app.include_router(forecasting.router, prefix=settings.API_V1_STR)

@app.get("/")
def system_heartbeat():
    return {
        "status": "online",
        "engine": settings.PROJECT_NAME,
        "environment": "active"
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from .database import engine, Base
# Import all models to register them on Base before create_all
from .domains.auth import models as auth_models
from .domains.organization import models as org_models
from .domains.hr import models as hr_models
from .domains.sales import models as sales_models
from .domains.operations import models as ops_models
from .domains.projects import models as proj_models

Base.metadata.create_all(bind=engine)

from .domains.auth.routers import router as auth_router
from .domains.organization.routers import router as org_router
from .domains.hr.routers import router as hr_router
from .domains.sales.routers import router as sales_router
from .domains.operations.routers import router as ops_router
from .domains.projects.routers import router as projects_router

app = FastAPI(title="AI-Powered ERP API", version="0.1.0")

# CORS_ORIGINS env var: comma-separated list of allowed origins (set in Render dashboard)
_extra_origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"] + _extra_origins,
    allow_origin_regex=r"https://.*\.vercel\.app",  # matches any Vercel preview/prod URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(org_router, prefix="/api/v1/organization", tags=["Organization"])
app.include_router(hr_router, prefix="/api/v1/hr", tags=["HR"])
app.include_router(sales_router, prefix="/api/v1/sales", tags=["Sales"])
app.include_router(ops_router, prefix="/api/v1/operations", tags=["Operations"])
app.include_router(projects_router, prefix="/api/v1/projects", tags=["Projects"])

from .ai_engine.routers import router as ai_router
app.include_router(ai_router, prefix="/api/v1/ai", tags=["AI"])

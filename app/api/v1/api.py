"""
Main API router.
"""
from fastapi import APIRouter

from app.api.v1.endpoints import auth, email, health, templates, tracking

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(email.router, prefix="/email", tags=["Email"])
api_router.include_router(templates.router, prefix="/templates", tags=["Templates"])
api_router.include_router(tracking.router, prefix="/tracking", tags=["Tracking"])
api_router.include_router(health.router, prefix="/health", tags=["Health"]) 
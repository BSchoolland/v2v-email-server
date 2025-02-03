"""
V2V Email Server - Main Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="V2V Email Server",
    description="A self-hosted email service infrastructure for managing email communications across multiple websites",
    version="0.1.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint returning service information."""
    return {
        "service": "V2V Email Server",
        "status": "operational",
        "version": "0.1.0",
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "components": {
            "api": "up",
            # These will be implemented later:
            # "database": "up",
            # "redis": "up",
            # "email": "up",
        }
    } 
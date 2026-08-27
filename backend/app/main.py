from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from . import models
from .routes.screening import router as screening_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="AI Resume Screener",
    description="AI-powered resume screening application",
    version="1.0.0"
)


# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
    "https://ai-resume-screener-project-plum.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(screening_router)


@app.get("/")
def root():
    return {
        "message": "AI Resume Screener API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

from fastapi import FastAPI

app = FastAPI(
    title="CaseCraft API",
    description="Backend API for the CaseCraft mystery investigation game.",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CaseCraft!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }

@app.get("/about")
def about_casecraft():
    return {
        "project":"CaseCraft",
        "purpose":"Mystery investigation game"
    }
    
@app.get("/game-status")
def game_status():
    return {
        "game":"CaseCraft",
        "status":"in development"
    }
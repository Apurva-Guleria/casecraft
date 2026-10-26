
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


class Case(BaseModel):
    id: int
    title: str
    description:str
    difficulty:str
    
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
    
@app.get("/cases", response_model=list[Case])
def get_cases():
    return [
        {
            "id":1,
            "title":"The Missing Diamond",
            "description":"A priceless diamond has disappeared from a museum.",
            "difficulty":"Easy"
        },
        {
                    "id":2,
                    "title":"The Silent Witness",
                    "description": "A key witness has mysteriously disappeared before giving evidence in a major case.",
                    "difficulty":"Medium"
                },
        {
                    "id":3,
                    "title":"The Midnight Murder",
                    "description": "A wealthy businessman has been found murdered in his mansion. Find the killer by examining clues and questioning suspects.",
                    "difficulty":"Hard"
                }
    ]
    

@app.get("/cases/{case_id}", response_model=Case)
def get_case(case_id: int):
    for case in get_cases():
        if case["id"] == case_id:
            return case

    raise HTTPException(
    status_code=404,
    detail="Case not found"
)

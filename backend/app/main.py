
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


class Case(BaseModel):
    id: int
    title: str
    description:str
    difficulty:str
    
class Suspect(BaseModel):
    id: int
    case_id: int
    name: str
    description: str
    is_guilty: bool
    
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

suspects = [
    {
        "id": 1,
        "case_id":1,
        "name": "Mr. Sharma",
        "description": "The museum manager who had access to the diamond room.",
        "is_guilty": False,
    },
    {
        "id": 2,
        "case_id":1,
        "name": "Riya Malhotra",
        "description": "A museum employee who was seen near the room.",
        "is_guilty": True,
    },
    {
        "id": 3,
        "case_id":1,
        "name": "Arjun Mehta",
        "description": "A security guard responsible for the night shift.",
        "is_guilty": False,
    },
    {
            "id": 4,
            "case_id": 2,
            "name": "Vikram Sethi",
            "description": "A colleague who was the last person to see the missing witness.",
            "is_guilty": False,
        },
        {
            "id": 5,
            "case_id": 2,
            "name": "Neha Kapoor",
            "description": "A close friend who may know why the witness disappeared.",
            "is_guilty": True,
        },
]

@app.get("/suspects", response_model=list[Suspect])
def get_suspects():
    return suspects

@app.get("/cases/{case_id}/suspects", response_model=list[Suspect])
def get_case_suspects(case_id: int):
    return [
        suspect
        for suspect in suspects
        if suspect["case_id"] == case_id
    ]
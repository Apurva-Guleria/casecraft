
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


class SuspectInternal(Suspect):
    is_guilty: bool
    
class Clue(BaseModel):
    id: int
    case_id: int
    title: str
    description: str
    is_important: bool

class Investigation(BaseModel):
    id: int
    case_id: int
    clue_id: int
    is_discovered: bool

class InvestigationUpdate(BaseModel):
    is_discovered: bool
     
class InvestigationSummary(BaseModel):
    case_id: int
    total_clues: int
    discovered_clues: int
    remaining_clues: int
    progress_percentage: float
    
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

clues = [
    {
        "id": 1,
        "case_id": 1,
        "title": "Broken Glass",
        "description": "A broken glass piece was found near the diamond display.",
        "is_important": True,
    },
    {
        "id": 2,
        "case_id": 1,
        "title": "Security Footage",
        "description": "A suspicious person was seen near the museum room.",
        "is_important": True,
    },
    {
        "id": 3,
        "case_id": 1,
        "title": "Visitor Register",
        "description": "The visitor register contains unusual entries.",
        "is_important": False,
    },
    {
        "id": 4,
        "case_id": 2,
        "title": "Last Phone Call",
        "description": "The missing witness received a mysterious phone call.",
        "is_important": True,
    },
]

investigations = [
    {
        "id": 1,
        "case_id": 1,
        "clue_id": 1,
        "is_discovered": True,
    },
    {
        "id": 2,
        "case_id": 1,
        "clue_id": 2,
        "is_discovered": False,
    },
    {
        "id": 3,
        "case_id": 1,
        "clue_id": 3,
        "is_discovered": False,
    },
    {
        "id": 4,
        "case_id": 2,
        "clue_id": 4,
        "is_discovered": True,
    },
]

@app.get("/suspects", response_model=list[Suspect])
def get_suspects():
    return suspects

@app.get("/clues",response_model=list[Clue])
def get_clues():
    return clues

@app.get("/clues/{clue_id}", response_model=Clue)
def get_clue(clue_id: int):

    for clue in clues:
        if clue["id"] == clue_id:
            return clue

    raise HTTPException(
        status_code=404,
        detail="Clue not found"
    )
    
@app.get("/cases/{case_id}/suspects", response_model=list[Suspect])
def get_case_suspects(case_id: int):

    case_exists = any(
        case["id"] == case_id
        for case in get_cases()
    )

    if not case_exists:
        raise HTTPException(
            status_code=404,
            detail="Case not found"
        )

    return [
        suspect
        for suspect in suspects
        if suspect["case_id"] == case_id
    ]

@app.get("/cases/{case_id}/clues", response_model=list[Clue])
def get_case_clues(case_id: int):

    case_exists = any(
        case["id"] == case_id
        for case in get_cases()
    )

    if not case_exists:
        raise HTTPException(
            status_code=404,
            detail="Case not found"
        )

    return [
        clue
        for clue in clues
        if clue["case_id"] == case_id
    ]    

@app.get("/cases/{case_id}/investigation",response_model=list[Investigation])
def get_investigation_progress(case_id: int):

    case_exists = any(
        case["id"] == case_id
        for case in get_cases()
    )

    if not case_exists:
        raise HTTPException(
            status_code=404,
            detail="Case not found"
        )

    return [
        investigation
        for investigation in investigations
        if investigation["case_id"] == case_id
    ]
  
@app.get(
    "/cases/{case_id}/investigation/summary",
    response_model=InvestigationSummary
)
def get_investigation_summary(case_id: int):

    case_exists = any(
        case["id"] == case_id
        for case in get_cases()
    )

    if not case_exists:
        raise HTTPException(
            status_code=404,
            detail="Case not found"
        )

    case_investigations = [
        investigation
        for investigation in investigations
        if investigation["case_id"] == case_id
    ]

    total_clues = len(case_investigations)

    discovered_clues = sum(
        1 for investigation in case_investigations
        if investigation["is_discovered"]
    )

    remaining_clues = total_clues - discovered_clues

    progress_percentage = (
        (discovered_clues / total_clues) * 100
        if total_clues > 0 else 0
    )

    return {
        "case_id": case_id,
        "total_clues": total_clues,
        "discovered_clues": discovered_clues,
        "remaining_clues": remaining_clues,
        "progress_percentage": round(progress_percentage, 2)
    }
      
@app.patch("/cases/{case_id}/investigation/{clue_id}",response_model = Investigation)
def update_investigation(
    case_id:int,
    clue_id:int,
    update_data:InvestigationUpdate
):
    for investigation in investigations:
        if(
            investigation["case_id"] == case_id
            and investigation["clue_id"] == clue_id
        ):
            investigation["is_discovered"] = update_data.is_discovered
            return investigation
    
    raise HTTPException(
        status_code = 404,
        detail = "Investigation record not found"
    )
            
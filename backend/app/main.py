from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.app.database import Base, engine,SessionLocal
from backend.app.models import CaseDB, SuspectDB,ClueDB,InvestigationDB

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

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CaseCraft API",
    description="Backend API for the CaseCraft mystery investigation game.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def seed_cases():
    db = SessionLocal()

    try:
        existing_cases = db.query(CaseDB).count()

        if existing_cases == 0:
            sample_cases = [
                CaseDB(
                    id=1,
                    title="The Missing Diamond",
                    description="A priceless diamond has disappeared from a museum.",
                    difficulty="Easy"
                ),
                CaseDB(
                    id=2,
                    title="The Silent Witness",
                    description="A key witness has mysteriously disappeared before giving evidence in a major case.",
                    difficulty="Medium"
                ),
                CaseDB(
                    id=3,
                    title="The Midnight Murder",
                    description="A wealthy businessman has been found murdered in his mansion. Find the killer by examining clues and questioning suspects.",
                    difficulty="Hard"
                )
            ]

            db.add_all(sample_cases)
            db.commit()
        existing_suspects = db.query(SuspectDB).count()

        if existing_suspects == 0:
            sample_suspects = [
                SuspectDB(
                    id=1,
                    case_id=1,
                    name="Mr. Sharma",
                    description="The museum manager who had access to the diamond room.",
                    is_guilty=False
                ),
                SuspectDB(
                    id=2,
                    case_id=1,
                    name="Riya Malhotra",
                    description="A museum employee who was seen near the room.",
                    is_guilty=True
                ),
                SuspectDB(
                    id=3,
                    case_id=1,
                    name="Arjun Mehta",
                    description="A security guard responsible for the night shift.",
                    is_guilty=False
                ),
                SuspectDB(
                    id=4,
                    case_id=2,
                    name="Vikram Sethi",
                    description="A colleague who was the last person to see the missing witness.",
                    is_guilty=False
                ),
                SuspectDB(
                    id=5,
                    case_id=2,
                    name="Neha Kapoor",
                    description="A close friend who may know why the witness disappeared.",
                    is_guilty=True
                )
            ]

            db.add_all(sample_suspects)
            db.commit()
            
        
        
        # Add clues for Case 3: The Midnight Murder
        existing_case_3_clues = db.query(ClueDB).filter(
            ClueDB.case_id == 3
        ).count()

        if existing_case_3_clues == 0:
            midnight_murder_clues = [
                ClueDB(
                    id=5,
                    case_id=3,
                    title="The Broken Whiskey Glass",
                    description="A shattered whiskey glass lies beside the victim's desk. Traces of an unknown substance are visible inside the glass.",
                    is_important=True
                ),
                ClueDB(
                    id=6,
                    case_id=3,
                    title="The Torn Letter",
                    description="A partially burned letter reveals a heated argument between the victim and someone close to him.",
                    is_important=True
                ),
                ClueDB(
                    id=7,
                    case_id=3,
                    title="The Stopped Clock",
                    description="The grandfather clock stopped at exactly 11:45 PM, potentially revealing the time of the incident.",
                    is_important=False
                )
            ]

            db.add_all(midnight_murder_clues)
            db.commit()
            
            
        # Add investigation records for Case 3
        existing_case_3_investigations = db.query(InvestigationDB).filter(
            InvestigationDB.case_id == 3
        ).count()

        if existing_case_3_investigations == 0:
            case_3_investigations = [
                InvestigationDB(
                    id=5,
                    case_id=3,
                    clue_id=5,
                    is_discovered=False
                ),
                InvestigationDB(
                    id=6,
                    case_id=3,
                    clue_id=6,
                    is_discovered=False
                ),
                InvestigationDB(
                    id=7,
                    case_id=3,
                    clue_id=7,
                    is_discovered=False
                )
            ]

            db.add_all(case_3_investigations)
            db.commit()


        

    finally:
        db.close()

seed_cases()

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
    db = SessionLocal()

    try:
        cases = db.query(CaseDB).all()
        return cases
    finally:
        db.close()

def case_exists(case_id: int):
    db = SessionLocal()

    try:
        return db.query(CaseDB).filter(
            CaseDB.id == case_id
        ).first() is not None

    finally:
        db.close()
        
@app.get("/cases/{case_id}", response_model=Case)
def get_case(case_id: int):
    db = SessionLocal()

    try:
        case = db.query(CaseDB).filter(
            CaseDB.id == case_id
        ).first()

        if case is None:
            raise HTTPException(
                status_code=404,
                detail="Case not found"
            )

        return case

    finally:
        db.close()


@app.get("/suspects", response_model=list[Suspect])
def get_suspects():
    db = SessionLocal()

    try:
        return db.query(SuspectDB).all()
    finally:
        db.close()

@app.get("/clues", response_model=list[Clue])
def get_clues():
    db = SessionLocal()

    try:
        return db.query(ClueDB).all()
    finally:
        db.close()

@app.get("/clues/{clue_id}", response_model=Clue)
def get_clue(clue_id: int):
    db = SessionLocal()
    try:
        clue = db.query(ClueDB).filter(
            ClueDB.id == clue_id
        ).first()

        if clue is None:
            raise HTTPException(
                status_code=404,
                detail="Clue not found"
            )

        return clue
    finally:
        db.close()
    
@app.get("/cases/{case_id}/suspects", response_model=list[Suspect])
def get_case_suspects(case_id: int):
    db = SessionLocal()

    try:
        if not db.query(CaseDB).filter(CaseDB.id == case_id).first():
            raise HTTPException(
                status_code=404,
                detail="Case not found"
            )

        return db.query(SuspectDB).filter(
            SuspectDB.case_id == case_id
        ).all()

    finally:
        db.close()
        
@app.get("/cases/{case_id}/clues", response_model=list[Clue])
def get_case_clues(case_id: int):
    db = SessionLocal()
    try:
        case = db.query(CaseDB).filter(
            CaseDB.id == case_id
        ).first()

        if case is None:
            raise HTTPException(
                status_code=404,
                detail="Case not found"
            )

        return db.query(ClueDB).filter(
            ClueDB.case_id == case_id
        ).all()

    finally:
        db.close()

@app.get("/cases/{case_id}/investigation", response_model=list[Investigation])
def get_investigation_progress(case_id: int):
    db = SessionLocal()

    try:
        case = db.query(CaseDB).filter(
            CaseDB.id == case_id
        ).first()

        if case is None:
            raise HTTPException(
                status_code=404,
                detail="Case not found"
            )

        return db.query(InvestigationDB).filter(
            InvestigationDB.case_id == case_id
        ).all()

    finally:
        db.close()
@app.get("/cases/{case_id}/investigation/summary", response_model=InvestigationSummary)
def get_investigation_summary(case_id: int):

    db = SessionLocal()

    try:
        case = db.query(CaseDB).filter(
            CaseDB.id == case_id
        ).first()

        if case is None:
            raise HTTPException(
                status_code=404,
                detail="Case not found"
            )

        case_investigations = db.query(InvestigationDB).filter(
            InvestigationDB.case_id == case_id
        ).all()

        total_clues = len(case_investigations)

        discovered_clues = sum(
            1 for investigation in case_investigations
            if investigation.is_discovered
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

    finally:
        db.close()
      
@app.patch(
    "/cases/{case_id}/investigation/{clue_id}",
    response_model=Investigation
)
def update_investigation(
    case_id: int,
    clue_id: int,
    update_data: InvestigationUpdate
):
    db = SessionLocal()

    try:
        investigation = db.query(InvestigationDB).filter(
            InvestigationDB.case_id == case_id,
            InvestigationDB.clue_id == clue_id
        ).first()

        if investigation is None:
            raise HTTPException(
                status_code=404,
                detail="Investigation record not found"
            )

        investigation.is_discovered = update_data.is_discovered

        db.commit()
        db.refresh(investigation)

        return investigation

    finally:
        db.close()
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to CaseCraft!",
        "status":"running",
    }
    
def test_health():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {
        "status":"healthy",
    }
    
def test_about():
    response = client.get("/about")
    
    assert response.status_code == 200
    assert response.json() == {
  "project": "CaseCraft",
  "purpose": "Mystery investigation game"
}
    
def test_game_status():
    response = client.get("/game-status")
    
    assert response.status_code == 200
    assert response.json() == {
  "game": "CaseCraft",
  "status": "in development"
}
    
def test_get_case_by_id():
    response = client.get("/cases/2")
    
    assert response.status_code == 200
    assert response.json()["title"] == "The Silent Witness"
    
def test_get_case_not_found():
    response = client.get("/cases/99")

    assert response.status_code == 404
    assert response.json()["detail"] == "Case not found"
    
def test_get_suspects_by_case_id():
    response = client.get("/cases/1/suspects")
    
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert all(
        suspect["case_id"] == 1
        for suspect in response.json()
    )
    
def test_get_suspects_for_case_2():
    response = client.get("/cases/2/suspects")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert all(
        suspect["case_id"] == 2
        for suspect in response.json()
    )
    
def test_suspects_for_nonexistent_case():
    response = client.get("/cases/99/suspects")

    assert response.status_code == 404
    assert response.json()["detail"] == "Case not found"
    
def test_get_all_clues():
    response = client.get("/clues")
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_get_clues_by_case_id():
    response = client.get("/cases/1/clues")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert all(
        clue["case_id"] == 1
        for clue in response.json()
    )


def test_get_clues_for_case_without_clues():
    response = client.get("/cases/3/clues")
    assert response.status_code == 200
    assert response.json() == []


def test_get_clues_for_nonexistent_case():
    response = client.get("/cases/99/clues")
    assert response.status_code == 404
    assert response.json()["detail"] == "Case not found"
    
def test_suspects_api_hides_guilty_status():
    response = client.get("/suspects")

    assert response.status_code == 200

    for suspect in response.json():
        assert "is_guilty" not in suspect
        
def test_case_suspects_api_hides_guilty_status():
    response = client.get("/cases/1/suspects")

    assert response.status_code == 200

    for suspect in response.json():
        assert "is_guilty" not in suspect
        
def test_get_clue_by_id():
    response = client.get("/clues/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Broken Glass"


def test_get_clue_not_found():
    response = client.get("/clues/99")

    assert response.status_code == 404
    assert response.json()["detail"] == "Clue not found"

def test_get_investigation_progress():
    response = client.get("/cases/1/investigation")

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_investigation_progress_for_case_2():
    response = client.get("/cases/2/investigation")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_investigation_progress_for_case_without_records():
    response = client.get("/cases/3/investigation")

    assert response.status_code == 200
    assert response.json() == []


def test_investigation_for_nonexistent_case():
    response = client.get("/cases/99/investigation")

    assert response.status_code == 404
    assert response.json()["detail"] == "Case not found"
    
def test_mark_clue_as_discovered():
    response = client.patch(
        "/cases/1/investigation/2",
        json={"is_discovered": True}
    )

    assert response.status_code == 200
    assert response.json()["is_discovered"] is True
    
def test_update_nonexistent_investigation():
    response = client.patch(
        "/cases/99/investigation/99",
        json={"is_discovered": True}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Investigation record not found"
    
def test_investigation_summary():
    response = client.get("/cases/1/investigation/summary")

    assert response.status_code == 200

    data = response.json()
    assert data["total_clues"] == 3
    assert data["discovered_clues"] == 2
    assert data["remaining_clues"] == 1
    assert data["progress_percentage"] == 66.67
    
def test_investigation_summary_without_records():
    response = client.get("/cases/3/investigation/summary")

    assert response.status_code == 200

    data = response.json()
    assert data["total_clues"] == 0
    assert data["discovered_clues"] == 0
    assert data["remaining_clues"] == 0
    assert data["progress_percentage"] == 0
    
def test_investigation_summary_not_found():
    response = client.get("/cases/99/investigation/summary")

    assert response.status_code == 404
    assert response.json()["detail"] == "Case not found"
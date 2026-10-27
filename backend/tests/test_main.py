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
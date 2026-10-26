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
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Penguin ML is running"}


def test_predict_endpoint(monkeypatch):
    # Monkeypatch predict function
    monkeypatch.setattr(
        'src.predict.predict',
        lambda data: 'Gentoo'
    )
    payload = {
        "culmen_length_mm": 50.0,
        "culmen_depth_mm": 15.0,
        "flipper_length_mm": 220.0,
        "body_mass_g": 4500.0
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    assert r.json() == {"predicted_species": "Gentoo"}
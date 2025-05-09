import pytest
from fastapi.testclient import TestClient
import src.app as app_module

client = TestClient(app_module.app)

@pytest.fixture(autouse=True)
def patch_predict(monkeypatch):
    # Replace the predict function used by the endpoint
    monkeypatch.setattr(
        app_module,
        'predict',
        lambda data: 'Gentoo'
    )
    yield


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Penguin ML is running"}


def test_predict_endpoint():
    payload = {
        "culmen_length_mm": 50.0,
        "culmen_depth_mm": 15.0,
        "flipper_length_mm": 220.0,
        "body_mass_g": 4500.0
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    assert r.json() == {"predicted_species": "Gentoo"}
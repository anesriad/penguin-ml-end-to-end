from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

class PenguinFeatures(BaseModel):
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Penguin ML is running"}

@app.post("/predict")
def predict_endpoint(features: PenguinFeatures):
    data = features.dict()
    species = predict(data)
    return {"predicted_species": species}
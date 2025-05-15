# src/app.py
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from src.predict import predict

class PenguinFeatures(BaseModel):
    culmen_length_mm:  float
    culmen_depth_mm:   float
    flipper_length_mm: float
    body_mass_g:       float

app = FastAPI()

# ————————————————————————————————————————————————————————————————
# 1) HTML form UI
# ————————————————————————————————————————————————————————————————

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head>
        <title>🐧 Penguin Classifier</title>
      </head>
      <body style="font-family:sans-serif;max-width:600px;margin:auto">
        <h1>Penguin Species Classifier</h1>
        <form action="/ui-predict" method="post">
          <label>Culmen length (mm):<br/>
            <input name="culmen_length_mm" type="number" step="0.1" required/>
          </label><br/><br/>

          <label>Culmen depth (mm):<br/>
            <input name="culmen_depth_mm" type="number" step="0.1" required/>
          </label><br/><br/>

          <label>Flipper length (mm):<br/>
            <input name="flipper_length_mm" type="number" step="0.1" required/>
          </label><br/><br/>

          <label>Body mass (g):<br/>
            <input name="body_mass_g" type="number" step="1" required/>
          </label><br/><br/>

          <button type="submit">Classify</button>
        </form>
      </body>
    </html>
    """

@app.post("/ui-predict", response_class=HTMLResponse)
def ui_predict(
    culmen_length_mm:  float = Form(...),
    culmen_depth_mm:   float = Form(...),
    flipper_length_mm: float = Form(...),
    body_mass_g:       float = Form(...),
):
    features = {
        "culmen_length_mm":  culmen_length_mm,
        "culmen_depth_mm":   culmen_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g":       body_mass_g,
    }
    species = predict(features)
    return f"""
    <html>
      <head>
        <title>Prediction Result</title>
      </head>
      <body style="font-family:sans-serif;max-width:600px;margin:auto">
        <h1>Predicted species:</h1>
        <p style="font-size:1.5em; font-weight:bold;">{species}</p>
        <a href="/">⇦ Classify another</a>
      </body>
    </html>
    """

# ————————————————————————————————————————————————————————————————
# 2) Your existing JSON API
# ————————————————————————————————————————————————————————————————

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(features: PenguinFeatures):
    data = features.dict()
    species = predict(data)
    return {"predicted_species": species}

# src/app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from .predict import predict

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body>
      <h1>Penguin Classifier</h1>
      <form action="/ui-predict" method="post">
        Culmen length (mm): <input name="culmen_length_mm" type="number" step="0.1"/><br/>
        Culmen depth  (mm): <input name="culmen_depth_mm"  type="number" step="0.1"/><br/>
        Flipper length: <input name="flipper_length_mm" type="number" step="0.1"/><br/>
        Body mass (g):   <input name="body_mass_g"       type="number" step="1"/><br/>
        <button type="submit">Classify</button>
      </form>
    </body>
    </html>
    """

@app.post("/ui-predict", response_class=HTMLResponse)
def ui_predict(
    culmen_length_mm: float = Form(...),
    culmen_depth_mm:  float = Form(...),
    flipper_length_mm: float = Form(...),
    body_mass_g:      float = Form(...),
):
    features = {
        "culmen_length_mm": culmen_length_mm,
        "culmen_depth_mm":  culmen_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g":       body_mass_g,
    }
    species = predict(features)
    return f"""
    <html>
    <body>
      <h1>Prediction: {species}</h1>
      <a href="/">Try another</a>
    </body>
    </html>
    """

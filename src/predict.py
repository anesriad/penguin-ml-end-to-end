import joblib
import pandas as pd
from pathlib import Path

# Mapping from integer code back to species name
SPECIES_MAP = {
    0: "Adelie",
    1: "Chinstrap",
    2: "Gentoo"
}

# Columns expected by the model
FEATURE_COLUMNS = [
    "culmen_length_mm",
    "culmen_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

# Resolve the location of the baked-in model relative to this file
BASE_DIR = Path(__file__).resolve().parents[1]  # /app
MODEL_PATH = BASE_DIR / "src" / "models" / "model.pkl"


def predict(input_data: dict) -> str:
    """
    Given a dictionary of features, load the model and return the predicted species name.
    Expects keys matching FEATURE_COLUMNS.
    """
    # Load the trained model from the baked-in artifact
    model = joblib.load(MODEL_PATH)

    # Create a DataFrame with a single row for prediction
    df = pd.DataFrame([input_data])
    X = df[FEATURE_COLUMNS]

    # Predict the integer code and map to species name
    code = model.predict(X)[0]
    return SPECIES_MAP.get(code, "Unknown")

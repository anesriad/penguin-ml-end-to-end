import joblib
import pandas as pd

# Mapping from integer code back to species name
SPECIES_MAP = {
    0: "Adelie",
    1: "Chinstrap",
    2: "Gentoo"
}

FEATURE_COLUMNS = [
    "culmen_length_mm",
    "culmen_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

def predict(
    input_data: dict,
    model_path: str = "mlruns/0/3bd7a8e4a29f4bc685e619654b97a486/artifacts/rf_model/model.pkl"
) -> str:
    """
    Given a dictionary of features, load the model and return the predicted species.
    Expects keys matching FEATURE_COLUMNS.
    """
    # Load model
    model = joblib.load(model_path)

    # Build DataFrame for prediction
    df = pd.DataFrame([input_data])
    X = df[FEATURE_COLUMNS]

    # Predict
    code = model.predict(X)[0]
    return SPECIES_MAP.get(code, "Unknown")
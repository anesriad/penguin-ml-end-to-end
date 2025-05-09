import pandas as pd


def preprocess(
    df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Clean and prepare the penguins DataFrame:
    - Drop rows missing target or key features
    - Encode species as integer labels
    - Select numeric feature columns

    Returns X (features) and y (target).
    """
    # Drop rows missing required columns
    clean = df.dropna(subset=[
        "species",
        "culmen_length_mm",
        "culmen_depth_mm",
        "flipper_length_mm",
        "body_mass_g"
    ]).copy()

    # Encode target
    clean["species_id"] = clean["species"].astype("category").cat.codes

    # Define features and target
    X = clean[[
        "culmen_length_mm",
        "culmen_depth_mm",
        "flipper_length_mm",
        "body_mass_g"
    ]]
    y = clean["species_id"]

    return X, y

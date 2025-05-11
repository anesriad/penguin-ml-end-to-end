from pathlib import Path
import pandas as pd

def load_data(
    raw_path: Path = Path(__file__).parents[1] / "penguins.csv",
    processed_path: Path = Path(__file__).parents[1] / "data" / "processed" / "penguins_clean.csv",
) -> pd.DataFrame:
    """
    Try loading the cleaned (processed) data first; if it doesn't exist,
    fall back to the raw CSV at the repo root.
    """
    if processed_path.is_file():
        return pd.read_csv(processed_path)
    elif raw_path.is_file():
        return pd.read_csv(raw_path)
    else:
        raise FileNotFoundError(
            f"Could not find either:\n"
            f" • processed data at {processed_path}\n"
            f" • raw data at {raw_path}"
        )

from pathlib import Path
import pandas as pd


def load_data(
    raw_path: Path | str = Path(__file__).parents[1] / "penguins.csv",
    processed_path: Path | str = Path(__file__).parents[1] / "data" / "processed" / "penguins_clean.csv",
) -> pd.DataFrame:
    """
    Load the processed dataset if available, otherwise load the raw CSV.

    Parameters
    ----------
    raw_path : Path or str
        Path to the raw data CSV (repo root)
    processed_path : Path or str
        Path to the cleaned data CSV

    Returns
    -------
    pd.DataFrame
    """
    # Ensure we have Path objects
    raw = Path(raw_path)
    proc = Path(processed_path)

    if proc.is_file():
        return pd.read_csv(proc)
    if raw.is_file():
        return pd.read_csv(raw)

    raise FileNotFoundError(
        f"Could not find data: neither '{{proc}}' nor '{{raw}}' exists."
    )
import pandas as pd


def load_data(
    raw_path: str = "/Users/riadanas/Desktop/penguin ML end2end/penguins.csv",
    processed_path: str = "/Users/riadanas/Desktop/penguin ML end2end/data/processed/penguins_clean.csv"
) -> pd.DataFrame:
    """
    Load the processed dataset if available, otherwise load the raw CSV.
    """
    try:
        df = pd.read_csv(processed_path)
    except FileNotFoundError:
        df = pd.read_csv(raw_path)
    return df
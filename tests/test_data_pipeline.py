import pandas as pd
from src.data_loader import load_data
from src.preprocess import preprocess

def test_load_data_raw(tmp_path):
    # Create a small CSV
    df_expected = pd.DataFrame({
        'species': ['A'],
        'culmen_length_mm': [10.0],
        'culmen_depth_mm': [5.0],
        'flipper_length_mm': [100.0],
        'body_mass_g': [3000.0]
    })
    file = tmp_path / "penguins.csv"
    df_expected.to_csv(file, index=False)
    # Call load_data with explicit raw_path
    df = load_data(raw_path=str(file), processed_path=str(tmp_path / "nonexistent.csv"))
    assert list(df.columns) == list(df_expected.columns)


def test_preprocess():
    df = pd.DataFrame({
        'species': ['A', None],
        'culmen_length_mm': [10.0, 20.0],
        'culmen_depth_mm': [5.0, None],
        'flipper_length_mm': [100.0, 200.0],
        'body_mass_g': [3000.0, 4000.0]
    })
    X, y = preprocess(df)
    # Only first row is valid
    assert X.shape[0] == 1
    assert y.iloc[0] == 0
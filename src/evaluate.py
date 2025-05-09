import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from src.data_loader import load_data
from src.preprocess import preprocess

def evaluate(model_path: str = "mlflow/mlruns/0/rf_model/model.pkl"):
    """
    Load a trained model and evaluate on the hold-out test set.
    Prints accuracy and full classification report.
    """
    # Load data
    df = load_data()
    X, y = preprocess(df)
    # Split matching train script
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Load model
    model = joblib.load(model_path)

    # Predict and evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    evaluate()
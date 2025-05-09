import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.data_loader import load_data
from src.preprocess import preprocess

def train():
    # Load and preprocess data
    df = load_data()
    X, y = preprocess(df)

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model parameters
    params = {"n_estimators": 100, "max_depth": 5}
    model = RandomForestClassifier(**params)

    # MLflow experiment
    with mlflow.start_run():
        mlflow.log_params(params)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "rf_model")
        print(f"Logged run with accuracy={acc:.4f}")

if __name__ == "__main__":
    train()
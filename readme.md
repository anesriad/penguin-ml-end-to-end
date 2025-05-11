![CI](https://github.com/anasriad8/penguin-ml-end-to-end/actions/workflows/ci.yml/badge.svg)
![Cloud Run](https://img.shields.io/badge/Cloud%20Run--Service-deployed-blue)

# Penguin ML End-to-End

Simple pipeline to train and serve a model that predicts penguin species.

## What We've Done So Far

Here's a summary of the steps completed up to now:

1. **Project Structure**  
   * Created core folders:  
     * `data/raw/`, `data/processed/`  
     * `notebooks/`  
     * `src/`  
     * `scripts/`  
     * `config/` (optional)  
     * `tests/` (optional)  
     * `mlflow/` (optional)  

2. **Core Files Added**  
   * `README.md` – overview of the project  
   * `.gitignore` – skip auto-generated or large files (e.g. `__pycache__/`, `.venv/`, `data/processed/`, `mlruns/`)  
   * `requirements.txt` – lists Python libraries: pandas, numpy, scikit-learn, fastapi, mlflow  

3. **Version Control**  
   * Initialized a Git repository (`git init`)  
   * Made the initial commit with project structure and core files  

4. **Dependency Management (UV)**  
   * Installed `uv-cli`  
   * Ran `uv init --name penguin-ml-end-to-end --python 3.11`  
   * Added packages with  
     ```bash
     uv add pandas numpy scikit-learn fastapi mlflow ipykernel pytest httpx
     ```  
   * Synced and activated the virtual environment (`uv sync` + `source .venv/bin/activate`)  

5. **Dockerfile**  
   * Created a `Dockerfile` based on `python:3.11-slim`  
   * Copied `requirements.txt` and installed dependencies  
   * Copied project files into `/app`  
   * Exposed port `8000`  
   * Set `CMD` to launch FastAPI via Uvicorn  

6. **MLflow Setup**  
   * Created `scripts/run_mlflow.sh` to launch MLflow UI (on port 5001)  
   * Instrumented `src/train.py` to:  
     * Load and preprocess the CSV data  
     * Train a RandomForest model  
     * Log hyperparameters, metrics, and model artifact to MLflow  
   * Tested MLflow UI and logs at [http://localhost:5001](http://localhost:5001)  

7. **Exploratory Data Analysis**  
   * Built a Jupyter notebook `notebooks/explore_penguins.ipynb`  
   * Loaded raw data, checked missing values, generated basic stats  
   * Plotted histograms, scatter plots, and species counts  
   * Saved cleaned data to `data/processed/penguins_clean.csv`  

8. **Modular Code Organization**  
   * `src/data_loader.py` – loads raw or cleaned data  
   * `src/preprocess.py` – drops rows with missing values, encodes labels, selects features  

9. **Training Script**  
   * `src/train.py` – ties together loader, preprocess, train/test split, model fit, MLflow logging  

10. **Evaluation Module**  
    * `src/evaluate.py` – loads the saved model, runs on hold-out set, prints accuracy and report  

11. **Prediction Logic**  
    * `src/predict.py` – loads model, takes a feature dict, returns the predicted species name  

12. **API Service**  
    * `src/app.py` – FastAPI app with:  
      * **GET /** health check  
      * **POST /predict** takes four features, returns the predicted species  

13. **Automated Tests**  
    * `tests/test_data_pipeline.py` – unit tests for data loading and preprocessing  
    * `tests/test_app.py` – endpoint tests with FastAPI’s TestClient  
    * Run with  
      ```bash
      pytest --maxfail=1 --disable-warnings -q
      ```  

14. **Continuous Integration**  
    * Added GitHub Actions workflow (`.github/workflows/ci.yml`) to:  
      1. Checkout code  
      2. Set up Python 3.11  
      3. Install UV (`pip install uv`)  
      4. Sync environment (`uv sync`)  
      5. Run tests (`uv run pytest --maxfail=1 --disable-warnings -q`)  
      6. Build Docker image (`docker build -t penguin-ml:end2end .`)  
      7. Log in to Docker Hub  
      8. Tag & push image to `anasriad8/penguin-ml:end2end`  

---

## Deployment

We’ve deployed the container to **GCP Cloud Run**. To reproduce:

1. **Build & push an amd64 image**  
   ```bash
   # ensure your gcloud is set to the right project
   PROJECT=$(gcloud config get-value project)

   # create and use a buildx builder
   docker buildx create --name multiarch-builder --use
   docker buildx inspect multiarch-builder --bootstrap

   # build & push for linux/amd64
   docker buildx build \
     --platform linux/amd64 \
     --push \
     -t gcr.io/$PROJECT/penguin-ml:end2end \
     .

   # Deploy to cloud Run:
   gcloud run deploy penguin-ml \
   --image gcr.io/$PROJECT/penguin-ml:end2end \
   --platform managed \
   --region us-central1 \
   --port 8000 \
   --allow-unauthenticated

   # Test the live endpoint
      curl -X POST \
      -H "Content-Type: application/json" \
      -d '{
       "culmen_length_mm": 50.0,
       "culmen_depth_mm": 15.0,
      "flipper_length_mm": 220.0,
      "body_mass_g": 4500.0
      }' \
      https://<YOUR_URL>/predict


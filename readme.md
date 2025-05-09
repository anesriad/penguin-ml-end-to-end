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
   * Added packages with `uv add pandas numpy scikit-learn fastapi mlflow ipykernel pytest`  
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
    * Run with `pytest --maxfail=1 --disable-warnings -q`  

---

## Next Steps

1. **Continuous Integration**  
   * Add a GitHub Actions workflow to install deps, run tests, lint code, and build the Docker image on every push.  

2. **Container Build & Push**  
   * Automate Docker image build and push to a registry (Docker Hub, ECR, GCR).  

3. **Detailed Documentation**  
   * Flesh out `README.md` with full setup, usage examples, API docs, and MLflow instructions.  

4. **Deployment**  
   * Deploy the Docker container to a cloud service (Heroku, AWS ECS/Fargate, GCP Cloud Run).  

5. **Monitoring & Alerts**  
   * Add basic logs, health checks, and optionally integrate a service like Sentry or Prometheus.

With this in place, anyone can clone the repo, follow the setup steps, and reproduce the entire workflow end to end. ```

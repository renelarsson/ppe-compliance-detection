# Copilot Instructions for PPE Compliance Detection

## Project Overview
This repository focuses on detecting Personal Protective Equipment (PPE) compliance using computer vision techniques. The project involves training models to identify whether individuals in images are wearing required safety gear (e.g., helmets, vests, gloves). The workflow includes data preprocessing, model training, evaluation, and deployment as a web service.

## Repository Structure
- **`markdown/`**: Contains project documentation, tips, and criteria.
- **`workshops/`**: Tutorials and guides for deploying models using various frameworks (e.g., FastAPI, Kubernetes).
- **`data/`**: Placeholder for datasets (not included in the repository).
- **`notebooks/`**: Jupyter notebooks for data exploration, training, and evaluation.
- **`service/`**: Code for serving the model as a FastAPI application.

## Key Workflows
### 1. Data Preparation
- Store datasets in the `data/` directory.
- Use Jupyter notebooks in `notebooks/` for data exploration and preprocessing.
- Ensure train/validation/test splits are created and saved in `data/`.

### 2. Model Training
- Implement training scripts in `notebooks/` or `service/train.py`.
- Use TensorFlow/Keras for model development.
- Save trained models in `service/` as `.h5` or `SavedModel` format.

### 3. Model Serving
- Use FastAPI for serving models.
- Define endpoints in `service/predict.py`:
  - `POST /predict`: Accepts image input and returns predictions.
  - `GET /health`: Returns a simple health check response.
- Containerize the service using Docker.

### 4. Deployment
- Deploy locally using Docker:
  ```bash
  docker build -t ppe-compliance .
  docker run -it -p 9696:9696 ppe-compliance
  ```
- Optionally deploy to cloud platforms (e.g., AWS, GCP).

## Project-Specific Conventions
- **Model Input**: Images resized to 224x224 pixels, normalized to [0, 1].
- **Model Output**: JSON object with detection scores and labels.
- **Dependencies**: Managed using `pyproject.toml` and `uv`.
- **Dockerization**: Use `python:3.13-slim` as the base image.

## Integration Points
- **TensorFlow/Keras**: For model training and inference.
- **FastAPI**: For building the web service.
- **Docker**: For containerization and deployment.
- **ONNX Runtime** (optional): For optimized inference on CPU.

## Examples
### FastAPI Endpoint Example
```python
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    img = Image.open(io.BytesIO(content))
    x = preprocess(img)
    y = model.predict(x)
    return {"scores": y[0].tolist()}
```

### Dockerfile Example
```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 9696
CMD ["uvicorn", "service.predict:app", "--host", "0.0.0.0", "--port", "9696"]
```

## Progress Tracking
- Maintain a log of progress and next steps in `markdown/progress-log.md`.
- Update the log after each session to ensure clear documentation of work completed and planned.

## Notes
- Follow the repository structure and naming conventions to ensure consistency.
- Document any new scripts or workflows in the `README.md` file.
- Use the `notebooks/` directory for experimentation and move finalized code to `service/`.

For further details, refer to the documentation in the `markdown/` directory.
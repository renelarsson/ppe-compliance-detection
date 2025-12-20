# Chest X-Ray Pneumonia

This project detects pneumonia in chest X-ray images using TensorFlow/Keras and serves predictions via a FastAPI web service.

## Quick Start

### Local (without Docker)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn service.predict:app --host 0.0.0.0 --port 9696
```

### Docker
```bash
docker build -t chest-xray-pneumonia .
docker run -it -p 9696:9696 chest-xray-pneumonia
```

## API
- GET /health → `{ "status": "ok" }`
- POST /predict → multipart `file` image; returns scores and input shape

## Next Steps
- Add training notebook in `notebooks/` to build a CNN with TensorFlow
- Save model to `service/` and load in `service/predict.py`
- Optionally export to ONNX and use CPU-optimized runtime
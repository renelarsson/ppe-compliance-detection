from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
import numpy as np

app = FastAPI()


def preprocess(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB").resize((224, 224))
    arr = np.asarray(image, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    img = Image.open(io.BytesIO(content))
    x = preprocess(img)
    # Placeholder prediction until a trained model is integrated
    scores = {"pneumonia": 0.0, "normal": 1.0}
    return {"scores": scores, "input_shape": list(x.shape)}

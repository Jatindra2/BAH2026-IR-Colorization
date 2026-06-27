from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import tempfile
import os

from backend.inference import predict_image
from backend.model_loader import load_models

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI(
    title="IRVision AI API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------------------
# Load Models Once
# --------------------------------------------------
sr_model, color_model = load_models()

print("Backend Ready")

# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "IRVision AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp:

        temp.write(await file.read())

        temp_path = temp.name

    output_path = predict_image(
        temp_path,
        sr_model,
        color_model,
    )

    return FileResponse(
        output_path,
        media_type="image/png",
        filename="prediction.png",
    )
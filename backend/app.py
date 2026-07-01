from pathlib import Path
import shutil
from backend.cleanup import remove_file

from backend.validators import (
    validate_file,
    validate_file_size,
)

from backend.logger import logger

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.inference import predict_image

from backend.config import (
    UPLOAD_DIR,
    OUTPUT_DIR,
    API_TITLE,
    API_VERSION,
)

from backend.config import ALLOWED_ORIGINS

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "IRVision AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = None

    try:

        # Validate upload
        validate_file(file)
        validate_file_size(file)

        logger.info(f"Uploading {file.filename}")

        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        output_path = OUTPUT_DIR / "prediction.png"

        result = predict_image(
            input_path=file_path,
            output_path=output_path,
        )

        logger.info("Prediction completed successfully")

        return result

    except HTTPException:
        raise

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        if file_path is not None:
            remove_file(file_path)

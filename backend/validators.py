from pathlib import Path

from fastapi import HTTPException

from backend.config import (
    SUPPORTED_EXTENSIONS,
    MAX_UPLOAD_SIZE,
)


def validate_file(file):

    extension = Path(file.filename).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Only {SUPPORTED_EXTENSIONS} files are supported."
        )


def validate_file_size(file):

    file.file.seek(0, 2)

    size = file.file.tell()

    file.file.seek(0)

    if size > MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Uploaded file exceeds maximum allowed size."
        )

from fastapi import FastAPI, UploadFile, File
import shutil
import os
from utils.parser import extract_text

app = FastAPI()

UPLOAD_DIR = "uploads"

@app.post("/upload-resume/")
def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)

    return {
        "filename": file.filename,
        "message": "Resume uploaded successfully",
        "preview": extracted_text[:500]  
    }



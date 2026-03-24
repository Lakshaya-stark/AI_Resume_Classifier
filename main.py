from fastapi import FastAPI, UploadFile, File
import shutil
import os
from utils.parser import extract_text
from utils.nlp import extract_skills   # 👈 NEW

app = FastAPI()

UPLOAD_DIR = "uploads"

@app.post("/upload-resume/")
def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)

    # 🔥 NLP processing
    skills = extract_skills(extracted_text)

    return {
        "filename": file.filename,
        "skills": skills,
        "preview": extracted_text[:300]
    }
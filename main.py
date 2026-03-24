from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
from utils.parser import extract_text
from utils.nlp import extract_skills
from utils.matcher import calculate_match_score
from db.mongo import candidates_collection



app = FastAPI()

UPLOAD_DIR = "uploads"


# Testing 
@app.get("/test-db")
def test_db():
    candidates_collection.insert_one({"test": "working"})
    return {"message": "MongoDB connected successfully"}



@app.post("/upload-resume/")
def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)
    skills = extract_skills(extracted_text)


    score = calculate_match_score(extracted_text, job_description, skills)

    return {
        "filename": file.filename,
        "skills": skills,
        "match_score": f"{score}%",
        "preview": extracted_text[:300]
    }


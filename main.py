from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
from utils.parser import extract_text
from utils.nlp import extract_skills
from utils.matcher import calculate_match_score
from db.mongo import candidates_collection  
from fastapi import Query
from fastapi import Body

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

UPLOAD_DIR = "uploads"

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


    candidate_data = {
    "filename": file.filename,
    "file_path": file_path,
    "skills": skills,
    "match_score": score,
    "job_description": job_description,
    "status": "pending",  
    "created_at": str(os.path.getctime(file_path))
}

    candidates_collection.insert_one(candidate_data)

    return {
        "filename": file.filename,
        "skills": skills,
        "match_score": f"{score}%"
    }

@app.get("/candidates")
def get_candidates(min_score: float = Query(0)):
    candidates = list(
        candidates_collection.find(
            {"match_score": {"$gte": min_score}},
            {"_id": 0}
        ).sort("match_score", -1)
    )
    return candidates



@app.put("/update-status")
def update_status(data: dict = Body(...)):
    filename = data.get("filename")
    status = data.get("status")

    result = candidates_collection.update_one(
        {"filename": filename},
        {"$set": {"status": status}}
    )

    if result.modified_count == 0:
        return {"message": "No document updated (check filename)"}

    return {"message": "Status updated successfully"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# AI-Based Resume Screening System (Backend)

## Overview

This backend service powers an AI-based resume screening system. It processes uploaded resumes, extracts relevant information using NLP, and ranks candidates based on job descriptions.

---

## Features

- Resume upload (PDF/DOCX)
- Text extraction and parsing
- Skill extraction using NLP (spaCy)
- Candidate-job matching using TF-IDF + skill scoring
- MongoDB integration for data storage
- Candidate ranking and filtering
- Status update (Shortlist / Reject)

---

## Tech Stack

- FastAPI
- MongoDB (pymongo)
- spaCy (NLP)
- scikit-learn (TF-IDF, similarity)
- PyPDF2 (PDF parsing)
- python-docx (DOCX parsing)

---

## Project Structure

│── main.py
│── utils/
│ ├── parser.py
│ ├── nlp.py
│ ├── matcher.py
│── db/
│ └── mongo.py
│── uploads/
│── requirements.txt

---

## Installation

### 1. Clone repository

git clone <repo-url>
cd backend

## 2.Create virtual environment

python3 -m venv venv
source venv/bin/activate

## 3. Install dependencies

pip install -r requirements.txt

## 4. Install spcCy Model

python -m spacy download en_core_web_sm

### Run Server

uvicorn main:app --reload

## API Endpoints

Upload Resume
POST /upload-resume/
Get Candidates
GET /candidates
Filter Candidates
GET /candidates?min_score=60
Update Status
PUT /update-status

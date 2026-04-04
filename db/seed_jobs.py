from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["resume_db"]
jobs = db["jobs"]


jobs.delete_many({})

jobs.insert_many([
    {
        "title": "Frontend Developer",
        "description": "Build UI using React, HTML, CSS, JavaScript",
        "skills": ["react", "javascript", "html", "css"]
    },
    {
        "title": "Backend Developer",
        "description": "Develop APIs using Node.js, Express, MongoDB, SQL",
        "skills": ["node", "express", "mongodb", "sql"]
    },
    {
        "title": "Full Stack Developer",
        "description": "Work on both frontend and backend using MERN stack",
        "skills": ["react", "node", "mongodb", "javascript"]
    },
    {
        "title": "Python Developer",
        "description": "Develop backend systems using Python, Django, Flask",
        "skills": ["python", "django", "flask", "sql"]
    },
    {
        "title": "DevOps Engineer",
        "description": "Manage infrastructure, CI/CD pipelines and cloud",
        "skills": ["docker", "kubernetes", "aws", "ci/cd"]
    },
    {
        "title": "Machine Learning Engineer",
        "description": "Build ML models and data pipelines",
        "skills": ["python", "machine learning", "tensorflow", "pandas"]
    }
])

print("✅ Jobs inserted successfully")
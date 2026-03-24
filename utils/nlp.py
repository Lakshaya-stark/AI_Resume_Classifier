import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "c++", "javascript",
    "react", "angular", "node", "django",
    "machine learning", "deep learning",
    "sql", "mongodb", "aws", "docker",
    "kubernetes", "git"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
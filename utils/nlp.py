import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = {
    "python": ["python"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "node": ["node", "node.js"],
    "react": ["react", "react.js"],
    "angular": ["angular"],
    "mongodb": ["mongodb", "mongo"],
    "sql": ["sql", "mysql", "postgresql"],
    "docker": ["docker"],
}
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill, variations in SKILLS_DB.items():
        for variation in variations:
            if variation in text:
                found_skills.append(skill)
                break

    return list(set(found_skills))
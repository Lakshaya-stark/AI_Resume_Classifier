from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description, extracted_skills):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    resume_combined = resume_text + " " + " ".join(extracted_skills)

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([job_description, resume_combined])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    score = similarity * 100
    final = round(score, 2)

    
    return round(score, 2) + 60
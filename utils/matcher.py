from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, job_description, resume_skills):

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    tfidf_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]


    job_description_lower = job_description.lower()

    matched_skills = [
        skill for skill in resume_skills if skill in job_description_lower
    ]

    if len(resume_skills) > 0:
        skill_score = len(matched_skills) / len(resume_skills)
    else:
        skill_score = 0

    final_score = (0.3 * tfidf_score) + (0.7 * skill_score)

    return round(final_score * 100, 2)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume, job_desc):
    documents = [resume, job_desc]
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(documents)
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])
    return round(similarity[0][0] * 100, 2)

def missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))
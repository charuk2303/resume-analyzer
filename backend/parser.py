import PyPDF2
from docx import Document
import os

# expanded skill list
SKILLS_DB = [
    "python", "java", "c++", "javascript", "html", "css", "react", "node.js",
    "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch",
    "data analysis", "pandas", "numpy", "sql", "mongodb", "postgresql",
    "aws", "docker", "kubernetes", "git", "linux", "agile", "scrum"
]

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if ext == ".pdf":
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")
    return text

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))
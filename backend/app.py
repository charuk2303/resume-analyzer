from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from parser import extract_text, extract_skills
from similarity import calculate_score, missing_skills

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "../uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# expanded job roles
JOB_ROLES = {
    "ml_engineer": {
        "desc": "Machine learning, python, data analysis, NLP, deep learning, tensorflow, pytorch",
        "skills": ["python", "machine learning", "nlp", "data analysis", "deep learning", "tensorflow", "pytorch"]
    },
    "web_dev": {
        "desc": "HTML, CSS, JavaScript, frontend development, react, node.js",
        "skills": ["html", "css", "javascript", "react", "node.js"]
    },
    "data_scientist": {
        "desc": "Python, data analysis, machine learning, SQL, pandas, numpy",
        "skills": ["python", "data analysis", "machine learning", "sql", "pandas", "numpy"]
    },
    "backend_dev": {
        "desc": "Python, Java, SQL, databases, APIs, docker",
        "skills": ["python", "java", "sql", "mongodb", "postgresql", "docker"]
    },
    "devops": {
        "desc": "AWS, Docker, Kubernetes, Linux, CI/CD, git",
        "skills": ["aws", "docker", "kubernetes", "linux", "git"]
    }
}

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        if "resume" not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files["resume"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400
        role = request.form.get("role")
        if not role or role not in JOB_ROLES:
            return jsonify({"error": "Invalid role selected"}), 400

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = extract_text(filepath)
        resume_skills = extract_skills(resume_text)

        job = JOB_ROLES[role]

        score = calculate_score(resume_text, job["desc"])
        missing = missing_skills(resume_skills, job["skills"])

        return jsonify({
            "score": score,
            "skills": resume_skills,
            "missing_skills": missing
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
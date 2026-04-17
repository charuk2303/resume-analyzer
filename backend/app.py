from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

from parser import extract_text, extract_skills
from similarity import calculate_score, missing_skills

app = Flask(__name__)
CORS(app)

# ✅ Upload folder setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ✅ Job roles
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

# ✅ Main API route
@app.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        # Check file
        if "resume" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["resume"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        # Check role
        role = request.form.get("role")
        if not role or role not in JOB_ROLES:
            return jsonify({"error": "Invalid role selected"}), 400

        # Save file securely
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Process resume
        resume_text = extract_text(filepath)
        resume_skills = extract_skills(resume_text)

        job = JOB_ROLES[role]

        # Calculate results
        score = calculate_score(resume_text, job["desc"])
        missing = missing_skills(resume_skills, job["skills"])

        # Response
        return jsonify({
            "score": score,
            "skills": resume_skills,
            "missing_skills": missing
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Run for deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
# AI Resume Analyzer

A web application that analyzes resumes against job descriptions using AI-powered text analysis and provides ATS (Applicant Tracking System) compatibility scores.

## Features

- **Multi-format Support**: Accepts PDF and DOCX resume files
- **Job Role Matching**: Analyzes resumes against multiple predefined job roles
- **Skill Extraction**: Automatically extracts relevant skills from resumes using NLP
- **ATS Scoring**: Calculates similarity scores between resume content and job descriptions
- **Missing Skills Identification**: Highlights skills that are missing for the selected role
- **Modern UI**: Clean, responsive web interface

## Supported Job Roles

- ML Engineer
- Web Developer
- Data Scientist
- Backend Developer
- DevOps Engineer

## Installation

1. Clone or download the project
2. Navigate to the project root directory
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Download the spaCy language model:
   ```
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Start the backend server:
   ```
   cd backend
   python app.py
   ```
   The server will run on http://127.0.0.1:5000

2. Open the frontend in a web browser:
   - Open `frontend/index.html` in your browser
   - Or serve it with a local server for better functionality

3. Upload a resume file (PDF or DOCX) and select a job role
4. Click "Analyze Resume" to get the results

## API Endpoints

### POST /upload
Uploads and analyzes a resume file.

**Parameters:**
- `resume`: File (PDF or DOCX)
- `role`: String (one of: ml_engineer, web_dev, data_scientist, backend_dev, devops)

**Response:**
```json
{
  "score": 75.5,
  "skills": ["python", "machine learning", "sql"],
  "missing_skills": ["tensorflow", "pytorch"]
}
```

## Technologies Used

- **Backend**: Flask, spaCy, scikit-learn, PyPDF2, python-docx
- **Frontend**: HTML, CSS, JavaScript
- **AI/ML**: Natural Language Processing for skill extraction, TF-IDF for text similarity

## Contributing

Feel free to add more job roles, improve the skill database, or enhance the analysis algorithms.
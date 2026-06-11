
# AI Resume vs Job Matcher

## Overview

AI Resume vs Job Matcher is a Python-based NLP application that helps job seekers evaluate how well their resume matches a specific job description. The system analyzes resume content, compares it with job requirements, calculates a match score, identifies missing skills, and provides suggestions for improvement.

This project demonstrates the use of Natural Language Processing (NLP), Machine Learning, and Streamlit for building an intelligent recruitment assistance tool.

---

## Features

* Upload resume in PDF format
* Paste job description
* Extract text from resume automatically
* Calculate Resume-Job Match Score
* Identify matching skills
* Identify missing skills
* Generate improvement suggestions
* User-friendly Streamlit interface

---

## Problem Statement

Job applicants often struggle to determine whether their resumes match the requirements of a job posting. Recruiters use Applicant Tracking Systems (ATS) to filter resumes based on relevant keywords and skills. Candidates may miss opportunities due to poor alignment between their resume and the job description.

The AI Resume vs Job Matcher addresses this issue by analyzing resumes and job descriptions, helping users identify skill gaps and improve their chances of getting shortlisted.

---

## Objectives

* Compare resumes with job descriptions
* Calculate a percentage-based match score
* Identify matching and missing skills
* Provide actionable resume improvement suggestions
* Improve ATS compatibility of resumes

---

## Technology Stack

| Component            | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| User Interface       | Streamlit                |
| PDF Processing       | PyPDF2                   |
| Machine Learning     | Scikit-learn             |
| NLP Techniques       | TF-IDF, Keyword Matching |
| Similarity Metric    | Cosine Similarity        |
| Data Processing      | Pandas                   |

---

## Project Structure

```text
resume_matcher/
│
├── app.py
├── matcher.py
├── skill_extractor.py
├── skills.txt
├── requirements.txt
└── README.md
```

---

## How It Works

### Step 1: Resume Upload

The user uploads a PDF resume.

### Step 2: Job Description Input

The user pastes the desired job description.

### Step 3: Text Extraction

The system extracts text from the uploaded resume using PyPDF2.

### Step 4: Skill Extraction

Skills are extracted from both the resume and job description using a predefined skills database.

### Step 5: Similarity Analysis

TF-IDF Vectorization converts text into numerical vectors.

### Step 6: Match Score Calculation

Cosine Similarity is used to calculate the similarity between the resume and job description.

### Step 7: Result Generation

The application displays:

* Match Score
* Matching Skills
* Missing Skills
* Improvement Suggestions

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume_matcher.git
cd resume_matcher
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## Sample Output

```text
Resume Match Score: 85%

Matching Skills:
✓ Python
✓ SQL
✓ Git

Missing Skills:
✗ Docker
✗ AWS

Suggestions:
• Learn Docker
• Add AWS certification
• Include cloud-based projects
```

---

## Future Enhancements

* ATS Score Analysis
* AI-Powered Resume Suggestions
* Resume Ranking System
* Multiple Resume Comparison
* Job Recommendation Engine
* Interactive Career Guidance Chatbot
* Cloud Deployment Support

---

## Applications

* Resume Screening
* Internship Preparation
* Placement Training
* Recruitment Assistance
* Career Guidance Platforms
* ATS Optimization

---

## Expected Outcome

The application helps users understand how well their resume aligns with a job description by providing:

* Resume Match Score
* Skill Gap Analysis
* Improvement Recommendations

This enables candidates to improve their resumes and increase their chances of securing interviews.

---

## Conclusion

AI Resume vs Job Matcher is an NLP-based recruitment assistance tool that leverages TF-IDF and Cosine Similarity to evaluate resume-job compatibility. It provides valuable insights into skill alignment and helps users optimize their resumes for better career opportunities.

---

## Author

Rutuja Kshirsagar

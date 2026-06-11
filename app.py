import streamlit as st
import PyPDF2

from matcher import calculate_match_score
from skill_extractor import load_skills
from skill_extractor import extract_skills


# -------------------------
# PDF Reader
# -------------------------

def extract_pdf_text(uploaded_file):

    text = ""

    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# -------------------------
# Streamlit UI
# -------------------------

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume vs Job Matcher")

st.write(
    "Upload your resume and compare it with a job description."
)

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if resume_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please enter job description.")
        st.stop()

    resume_text = extract_pdf_text(resume_file)

    score = calculate_match_score(
        resume_text,
        job_description
    )

    skills_db = load_skills()

    resume_skills = extract_skills(
        resume_text,
        skills_db
    )

    job_skills = extract_skills(
        job_description,
        skills_db
    )

    matching_skills = list(
        set(resume_skills).intersection(job_skills)
    )

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    st.subheader("Match Score")

    st.progress(min(int(score), 100))

    st.metric(
        label="Resume Match %",
        value=f"{score}%"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matching Skills")

        if matching_skills:
            for skill in matching_skills:
                st.success(skill)

        else:
            st.warning("No matching skills found.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)

        else:
            st.success("No missing skills.")

    st.subheader("💡 Suggestions")

    if missing_skills:

        for skill in missing_skills:
            st.write(
                f"• Consider adding or learning {skill}"
            )

    else:
        st.success(
            "Your resume matches most required skills."
        )
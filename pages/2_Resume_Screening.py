import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

# ===============================
# IMPORT YOUR EXISTING MODULES
# ===============================
from components.header import show_header
from components.candidate_card import show_candidate

from resume_parser import extract_text_from_pdf

from nlp_extractor import (
    extract_jd_skills,
    extract_name,
    extract_email,
    extract_phone,
    extract_education,
    extract_experience
)

from matcher import (
    match_skills,
    normalize_skills,
    jd_similarity
)

from scorer import calculate_score, classify

from ai_engine import ai_extract_skills
from utils.skill_list import ALL_SKILLS


# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)

# ===============================
# CUSTOM CSS
# ===============================
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #1f4e79;
}

.stButton>button {
    background-color: #1f77ff;
    color: white;
    border-radius: 10px;
    height: 45px;
    border: none;
    font-weight: bold;
    width: 100%;
}

.stButton>button:hover {
    background-color: #125dcc;
    color: white;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}

.stTextArea textarea {
    border-radius: 10px;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}

.css-1r6slb0 {
    background-color: white;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# SESSION STATE
# ===============================
if "results" not in st.session_state:
    st.session_state.results = []

# ===============================
# SAFE SKILL EXTRACTION
# ===============================
def safe_ai_extract(text, jd_skills=None):

    text_clean = text.lower()
    text_clean = re.sub(r"[^\w\s]", " ", text_clean)

    # Rule-based skills
    rule_skills = [s for s in ALL_SKILLS if s in text_clean]

    # AI-based extraction
    try:
        ai_skills = ai_extract_skills(text)
        ai_skills = [s for s in ai_skills if s in text_clean]
    except:
        ai_skills = []

    combined = list(set(rule_skills + ai_skills))

    if jd_skills:
        filtered = [s for s in combined if s in jd_skills]
        return filtered if filtered else combined

    return combined

# ===============================
# HEADER
# ===============================
show_header()

# ===============================
# TOP NAVIGATION
# ===============================
menu = st.radio(
    "",
    ["Resume Screening", "Dashboard", "Analytics"],
    horizontal=True
)

# =========================================================
# RESUME SCREENING PAGE
# =========================================================
if menu == "Resume Screening":

    st.header("🧾 Resume Screening")

    col1, col2 = st.columns(2)

    with col1:
        required_skills_input = st.text_input(
            "Required Skills (comma separated)"
        )

    with col2:
        uploaded_files = st.file_uploader(
            "Upload Resumes",
            type="pdf",
            accept_multiple_files=True
        )

    jd_text = st.text_area(
        "Job Description",
        height=180
    )

    # ===============================
    # PROCESS BUTTON
    # ===============================
    if st.button("🚀 Analyze Resumes"):

        if not uploaded_files:
            st.warning("Please upload resumes.")
        
        elif not jd_text:
            st.warning("Please enter Job Description.")

        else:

            # Clear previous results
            st.session_state.results = []

            # Normalize required skills
            required_skills = normalize_skills(
                required_skills_input.split(",")
            )

            jd_skills = extract_jd_skills(jd_text)

            # ===============================
            # PROCESS EACH RESUME
            # ===============================
            for file in uploaded_files:

                text = extract_text_from_pdf(file)

                # ---------------------------
                # NLP EXTRACTION
                # ---------------------------
                name = extract_name(text)
                email = extract_email(text)
                phone = extract_phone(text)
                education = extract_education(text)
                experience = extract_experience(text)

                # ---------------------------
                # SKILL EXTRACTION
                # ---------------------------
                skills = safe_ai_extract(text, jd_skills)
                skills = normalize_skills(skills)

                matched = match_skills(
                    skills,
                    required_skills
                )

                # ---------------------------
                # SCORING
                # ---------------------------

                # Skill Score = 35%
                skill_score = min(len(matched) * 10, 100)

                # JD Similarity = 35%
                jd_score = jd_similarity(jd_text, text)

                # Education Score = 20%
                education_score = 80 if education else 40

                # Experience Score = 10%
                experience_score = min(experience * 10, 100)

                # FINAL SCORE
                final_score = calculate_score(
                    skill_score,
                    jd_score,
                    education_score,
                    experience_score
                )

                result = classify(final_score)

                # WHY SELECTED
                why_selected = f"""
Matched Skills: {', '.join(matched[:5])}

JD Similarity: {round(jd_score, 2)}%

Education: {education}

Experience: {experience} years
"""

                # STORE RESULT
                st.session_state.results.append({

                    "Name": name if name else file.name,

                    "Email": email,

                    "Phone": phone,

                    "Education": str(education),

                    "Experience": experience,

                    "Skills": ", ".join(skills),

                    "Matched Skills": ", ".join(matched),

                    "Skill Score": round(skill_score, 2),

                    "JD Score": round(jd_score, 2),

                    "Education Score": round(education_score, 2),

                    "Experience Score": round(experience_score, 2),

                    "Total Score": round(final_score, 2),

                    "Result": result,

                    "Why Selected": why_selected
                })

            st.success("✅ Resume Analysis Completed!")

    # ===============================
    # DISPLAY RESULTS
    # ===============================
    if st.session_state.results:

        df = pd.DataFrame(st.session_state.results)

        st.subheader("🏆 Candidate Ranking")

        ranked_df = df.sort_values(
            by="Total Score",
            ascending=False
        )

        st.dataframe(
            ranked_df,
            use_container_width=True
        )

        st.subheader("🎯 Candidate Profiles")

        for _, row in ranked_df.iterrows():
            show_candidate(row)

# =========================================================
# DASHBOARD PAGE
# =========================================================
elif menu == "Dashboard":

    st.header("📊 Dashboard")

    df = pd.DataFrame(st.session_state.results)

    if df.empty:
        st.info("No resume analysis available.")

    else:

        total_candidates = len(df)

        selected = len(
            df[df["Result"] == "Selected"]
        )

        rejected = len(
            df[df["Result"] == "Rejected"]
        )

        avg_score = round(
            df["Total Score"].mean(),
            2
        )

        # ===============================
        # METRICS
        # ===============================
        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Candidates",
            total_candidates
        )

        col2.metric(
            "Selected",
            selected
        )

        col3.metric(
            "Rejected",
            rejected
        )

        col4.metric(
            "Average Score",
            avg_score
        )

        st.divider()

        # ===============================
        # TOP PERFORMERS
        # ===============================
        st.subheader("🏆 Top Candidates")

        top_df = df.sort_values(
            by="Total Score",
            ascending=False
        )

        st.dataframe(
            top_df[
                [
                    "Name",
                    "Total Score",
                    "Matched Skills",
                    "Result"
                ]
            ],
            use_container_width=True
        )

# =========================================================
# ANALYTICS PAGE
# =========================================================
elif menu == "Analytics":

    st.header("📈 Resume Analytics")

    df = pd.DataFrame(st.session_state.results)

    if df.empty:
        st.info("No analytics available.")

    else:

        # ===============================
        # SCORE DISTRIBUTION
        # ===============================
        st.subheader("📊 Score Distribution")

        fig1, ax1 = plt.subplots(figsize=(8, 4))

        ax1.hist(df["Total Score"])

        ax1.set_xlabel("Score")
        ax1.set_ylabel("Candidates")

        st.pyplot(fig1)

        # ===============================
        # SKILL VS JD SCORE
        # ===============================
        st.subheader("🧠 Skill Score vs JD Score")

        fig2, ax2 = plt.subplots(figsize=(8, 4))

        ax2.scatter(
            df["Skill Score"],
            df["JD Score"]
        )

        ax2.set_xlabel("Skill Score")
        ax2.set_ylabel("JD Score")

        st.pyplot(fig2)

        # ===============================
        # TOP SKILLS
        # ===============================
        st.subheader("🔥 Top Skills")

        all_skills = []

        for skill_text in df["Matched Skills"]:
            skill_list = skill_text.split(",")

            for s in skill_list:
                s = s.strip()

                if s:
                    all_skills.append(s)

        skill_counts = pd.Series(
            all_skills
        ).value_counts().head(10)

        fig3, ax3 = plt.subplots(figsize=(8, 4))

        ax3.bar(
            skill_counts.index,
            skill_counts.values
        )

        plt.xticks(rotation=45)

        st.pyplot(fig3)

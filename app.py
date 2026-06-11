# =====================================================
# APP.PY
# AI RESUME SCREENING SYSTEM
# =====================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

# =====================================================
# IMPORTS
# =====================================================

from components.header import show_header
from components.candidate_card import show_candidate

# from auth import (
#     signup_user,
#     login_user
# )
from auth import (
    signup_user,
    login_user,
    save_candidate
)

from resume_parser import extract_text_from_pdf

from utils.skill_list import (
    ALL_SKILLS,
    SKILLS_DB
)

from nlp_extractor import (
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

from scorer import (
    calculate_score,
    classify
)

from ai_engine import ai_reason_selection


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "results" not in st.session_state:
    st.session_state.results = []

if "jd_text" not in st.session_state:
    st.session_state.jd_text = ""

if "required_skills" not in st.session_state:
    st.session_state.required_skills = ""

if "uploaded_resume_names" not in st.session_state:
    st.session_state.uploaded_resume_names = []

if "uploaded_resume_data" not in st.session_state:
    st.session_state.uploaded_resume_data = []


# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged_in:

    # =================================================
    # LOGIN CSS
    # =================================================
    st.markdown("""
    <style>

    /* =========================
        GLOBAL APP STYLING
    ========================= */

    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    /* Main App Background */
    .stApp {
        background: linear-gradient(to bottom right, #0b1026, #101935);
        color: white;
    }

    /* =========================
        LIGHT MODE SUPPORT
    ========================= */

    @media (prefers-color-scheme: light) {

        .stApp {
            background: #f4f6fb !important;
            color: #111111 !important;
        }

        h1, h2, h3, h4, h5, h6,
        p, span, label, div {
            color: #111111 !important;
        }

        /* Cards / Containers */
        .block-container,
        div[data-testid="stVerticalBlock"] {
            background-color: #ffffff !important;
            color: #111111 !important;
            border-radius: 12px;
        }

        /* Input Fields */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div,
        .stNumberInput input {
            background-color: #ffffff !important;
            color: #111111 !important;
            border: 1px solid #cccccc !important;
        }

        /* Tables */
        table {
            background-color: white !important;
            color: black !important;
        }

        thead tr th {
            background-color: #dbe4ff !important;
            color: black !important;
        }

        tbody tr td {
            color: black !important;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #4a6cf7, #5cb8ff);
            color: white !important;
            border: none;
            border-radius: 10px;
        }
    }

    /* =========================
        DARK MODE SUPPORT
    ========================= */

    @media (prefers-color-scheme: dark) {

        .stApp {
            background: linear-gradient(to bottom right, #050816, #0b1026);
            color: white !important;
        }

        h1, h2, h3, h4, h5, h6,
        p, span, label, div {
            color: white !important;
        }
    

        /* Cards / Containers */
        .block-container,
        div[data-testid="stVerticalBlock"] {
            background-color: #111827 !important;
            color: white !important;
            border-radius: 12px;
        }

        /* Input Fields */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div,
        .stNumberInput input {
            background-color: #1f2937 !important;
            color: white !important;
            border: 1px solid #374151 !important;
        }

        /* Tables */
        table {
            background-color: #111827 !important;
            color: white !important;
        }

        thead tr th {
            background-color: #1f2937 !important;
            color: white !important;
        }

        tbody tr td {
            color: white !important;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #4a6cf7, #5cb8ff);
            color: white !important;
            border: none;
            border-radius: 10px;
        }
    }

    /* =========================
        SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* =========================
        SUCCESS / ERROR BOXES
    ========================= */

    .stAlert {
        border-radius: 10px;
    }

    /* =========================
        DATAFRAME
    ========================= */

    [data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
    }


    /* -----------------------------
        ADD THIS AT THE BOTTOM
    ------------------------------ */

    /* Download button text fix */
    .stDownloadButton > button {
        color: white !important;
    }

    /* Uploaded file text */
    [data-testid="stFileUploaderFileName"] {
        color: white !important;
    }

    /* Light mode support */
    @media (prefers-color-scheme: light) {

        .stDownloadButton > button {
            color: black !important;
            background-color: #dbeafe !important;
        }

        [data-testid="stFileUploaderFileName"] {
            color: black !important;
        }
    }


    </style>
    """, unsafe_allow_html=True)
  
    # =================================================
    # CENTER LOGIN BOX
    # =================================================

    col1, col2, col3 = st.columns([1.2, 1.5, 1.2])

    with col2:

        st.markdown("""
        <div class="auth-container">

        <div class="auth-title">
        AI Resume Screening System
        </div>

        <div class="auth-subtitle">
        Smart AI-Powered Applicant Tracking System
        </div>

        """, unsafe_allow_html=True)

        auth_option = st.radio(
            "Choose Option",
            ["Login", "Signup"],
            horizontal=True
        )

        email = st.text_input(
            "Email Address"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        # =============================================
        # SIGNUP
        # =============================================

        if auth_option == "Signup":
            role = st.selectbox(
                "Select Role",
                [
                    "Admin",
                    "Recruiter",
                    "HR Manager"
                ]
            )

            if st.button(
                "Create Account",
                use_container_width=True
            ):
               

                success = signup_user(
                    email,
                    password,
                    role
                )
                

                if success:

                    st.success(
                        "Account created successfully!"
                    )

                else:

                    st.error(
                        "Email already exists."
                    )

        # =============================================
        # LOGIN
        # =============================================

        else:

            if st.button(
                "Login",
                use_container_width=True
            ):

                user = login_user(
                    email,
                    password
                )

                if user:

                    st.session_state.logged_in = True

                    st.session_state.user_email = email
                    st.session_state.role = user[3]

                    st.success(
                        "Login successful!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid email or password."
                    )

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()


# =====================================================
# SHOW HEADER AFTER LOGIN
# =====================================================

show_header()

# =========================================
# TOP BAR
# =========================================

top1, top2 = st.columns([6,1])

with top1:

    st.success(
        f"Logged in as: {st.session_state.role}"
    )

with top2:

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.user_email = ""

        st.session_state.role = ""

        st.rerun()

# =====================================================
# MAIN APP CSS
# =====================================================

st.markdown("""
<style>

/* =========================================
   GLOBAL APP STYLING
========================================= */

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* Main App Background */
.stApp {
    background: linear-gradient(135deg, #020617, #0b1120);
    color: white;
}

/* =========================================
   HEADINGS
========================================= */

h1, h2, h3, h4, h5, h6 {
    color: #60a5fa !important;
    font-weight: 700 !important;
}

/* =========================================
   SIDEBAR
========================================= */

section[data-testid="stSidebar"] {
    background: #111827 !important;
    color: white !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* =========================================
   INPUT FIELDS
========================================= */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox div,
.stMultiSelect div {
    background-color: #1e293b !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

/* =========================================
   BUTTONS
========================================= */

.stButton button {
    background: linear-gradient(90deg, #4f46e5, #38bdf8) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: 600 !important;
    transition: 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #2563eb, #0ea5e9) !important;
}

/* =========================================
   DOWNLOAD BUTTON FIX
========================================= */

.stDownloadButton button {
    background: #1f2937 !important;
    color: #ffffff !important;
    border: 1px solid #3b82f6 !important;
    border-radius: 10px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important;
}

.stDownloadButton button:hover {
    background: #2563eb !important;
    color: white !important;
}

/* =========================================
   FILE UPLOADER FIX
========================================= */

/* Upload Box */
section[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

/* Upload Text */
section[data-testid="stFileUploader"] * {
    color: #ffffff !important;
}

/* Uploaded File Names */
[data-testid="stFileUploaderFileName"] {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* =========================================
   DATAFRAMES / TABLES
========================================= */

[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden;
}

table {
    background-color: #111827 !important;
    color: white !important;
}

thead tr th {
    background-color: #1e293b !important;
    color: #60a5fa !important;
}

/* =========================================
   CARDS / CONTAINERS
========================================= */

.candidate-card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 20px;
    color: white !important;
}

/* =========================================
   SUCCESS / ERROR MESSAGES
========================================= */

.stSuccess {
    background-color: rgba(34,197,94,0.2) !important;
    color: #4ade80 !important;
    border-radius: 10px !important;
}

.stError {
    background-color: rgba(239,68,68,0.2) !important;
    color: #f87171 !important;
    border-radius: 10px !important;
}

/* =========================================
   METRICS
========================================= */

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 15px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* =========================================
   LIGHT MODE SUPPORT
========================================= */

@media (prefers-color-scheme: light) {

    /* Main Background */
    .stApp {
        background: #f3f4f6 !important;
        color: #111111 !important;
    }

    /* Global Text */
    html, body, [class*="css"] {
        color: #111111 !important;
    }

    /* Inputs */
    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input,
    .stSelectbox div,
    .stMultiSelect div {
        background-color: white !important;
        color: black !important;
        border: 1px solid #cbd5e1 !important;
    }

    /* Tables */
    table {
        background-color: white !important;
        color: black !important;
    }

    thead tr th {
        background-color: #dbeafe !important;
        color: black !important;
    }

    /* Download Button */
    .stDownloadButton button {
        background: #dbeafe !important;
        color: #000000 !important;
        border: 1px solid #2563eb !important;
    }

    .stDownloadButton button:hover {
        background: #2563eb !important;
        color: white !important;
    }

    /* File Upload */
    section[data-testid="stFileUploader"] {
        background: #ffffff !important;
    }

    section[data-testid="stFileUploader"] * {
        color: #000000 !important;
    }

    [data-testid="stFileUploaderFileName"] {
        color: #000000 !important;
    }

    /* Cards */
    .candidate-card {
        background: white !important;
        color: black !important;
        border: 1px solid #d1d5db !important;
    }

    /* Metrics */
    [data-testid="metric-container"] {
        background: white !important;
        color: black !important;
        border: 1px solid #d1d5db !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #e5e7eb !important;
    }

    section[data-testid="stSidebar"] * {
        color: black !important;
    }
}

</style>
""", unsafe_allow_html=True)
# =====================================================
# DETECT DOMAIN
# =====================================================

def detect_domain(jd_text):

    jd_lower = jd_text.lower()

    domain_scores = {}

    for domain, skills in SKILLS_DB.items():

        score = 0

        for skill in skills:

            if skill.lower() in jd_lower:
                score += 1

        domain_scores[domain] = score

    best_domain = max(
        domain_scores,
        key=domain_scores.get
    )

    return best_domain


# =====================================================
# FORMAT EDUCATION
# =====================================================

def format_education(education_df):

    try:

        if education_df.empty:
            return "Not Available"

        formatted = []

        for _, row in education_df.iterrows():

            qualification = str(
                row["Qualification"]
            ).strip()

            percentage = str(
                row["Percentage"]
            ).strip()

            formatted.append(
                f"{qualification} - {percentage}%"
            )

        return " | ".join(formatted)

    except:
        return "Not Available"


# =========================================
# ROLE BASED MENUS
# =========================================

if st.session_state.role == "Admin":

    menu = st.radio(
        "",
        [
            "Resume Screening",
            "Dashboard",
            "Analytics",
            "AI Chatbot",
            "Manage Users"
        ],
        horizontal=True
    )

elif st.session_state.role == "Recruiter":

    menu = st.radio(
        "",
        [
            "Resume Screening",
            "Dashboard",
            "AI Chatbot"
        ],
        horizontal=True
    )

elif st.session_state.role == "HR Manager":

    menu = st.radio(
        "",
        [
            "Dashboard",
            "Analytics"
        ],
        horizontal=True
    )


# =====================================================
# RESUME SCREENING
# =====================================================

if menu == "Resume Screening":

    st.header("🧾 AI Resume Screening")

    col1, col2 = st.columns(2)

    # =================================================
    # REQUIRED SKILLS
    # =================================================

    with col1:

        required_skills_input = st.text_input(
            "Required Skills",
            value=st.session_state.required_skills
        )

        st.session_state.required_skills = (
            required_skills_input
        )

    # =================================================
    # FILE UPLOADER
    # =================================================

    with col2:

        uploaded_files = st.file_uploader(
            "Upload Resume PDFs",
            type=["pdf"],
            accept_multiple_files=True
        )

        if uploaded_files:

            st.session_state.uploaded_resume_names = [
                file.name for file in uploaded_files
            ]

            st.session_state.uploaded_resume_data = (
                uploaded_files
            )

    # =================================================
    # SHOW UPLOADED FILES
    # =================================================

    if st.session_state.uploaded_resume_names:

        st.success("Uploaded Resumes")

        for file_name in st.session_state.uploaded_resume_names:

            st.write(f"✅ {file_name}")

    # =================================================
    # JOB DESCRIPTION
    # =================================================

    jd_text = st.text_area(
        "Job Description",
        value=st.session_state.jd_text,
        height=250
    )

    st.session_state.jd_text = jd_text

    # =================================================
    # ANALYZE
    # =================================================

    if st.button("🚀 Analyze Resumes"):

        uploaded_files = (
            st.session_state.uploaded_resume_data
        )

        if not uploaded_files:

            st.warning(
                "Please upload resumes."
            )

        elif not jd_text:

            st.warning(
                "Please enter Job Description."
            )

        else:

            st.session_state.results = []

            required_skills = normalize_skills(
                required_skills_input.split(",")
            )

            detected_domain = detect_domain(
                jd_text
            )

            domain_skills = SKILLS_DB[
                detected_domain
            ]

            # =========================================
            # PROCESS RESUMES
            # =========================================

            for file in uploaded_files:

                text = extract_text_from_pdf(file)

                name = extract_name(text)

                email = extract_email(text)

                phone = extract_phone(text)

                education = extract_education(text)

                experience = extract_experience(text)

                # =====================================================
                # SAVE PDF FILE
                # =====================================================

                upload_folder = "uploads"

                if not os.path.exists(upload_folder):

                    os.makedirs(upload_folder)

                resume_path = os.path.join(
                    upload_folder,
                    file.name
                )

                with open(resume_path, "wb") as f:

                    f.write(file.getbuffer())

                # ======================================
                # ADVANCED SKILL EXTRACTION
                # ======================================

                

                text_lower = text.lower()

                skills = []

                for skill in ALL_SKILLS:

                    # Create regex pattern
                    pattern = r'\b' + re.escape(skill.lower()) + r'\b'

                    # Exact word matching
                    if re.search(pattern, text_lower):

                        skills.append(skill.lower())

                # ======================================
                # REMOVE DUPLICATES
                # ======================================

                skills = list(set(skills))

                # ======================================
                # NORMALIZE
                # ======================================

                skills = normalize_skills(skills)

                # ======================================
                # SORT SKILLS
                # ======================================

                skills = sorted(skills)

                # =====================================
                # MATCHING
                # =====================================

                matched = match_skills(
                    skills,
                    required_skills
                )

                missing_skills = list(
                    set(required_skills) -
                    set(matched)
                )

                jd_score = jd_similarity(
                    jd_text,
                    text
                )

                # =====================================
                # FINAL SCORE
                # =====================================

                skill_score, edu_score, exp_score, final_score = calculate_score(
                    matched,
                    required_skills,
                    education,
                    experience,
                    jd_score
                )

                result = classify(final_score)

                # =====================================
                # AI ANALYSIS
                # =====================================

                why_selected = ai_reason_selection(

                    text,

                    jd_text,

                    matched,

                    missing_skills,

                    experience,

                    final_score,

                    result
                )

                # =====================================================
                # SAVE CANDIDATE TO DATABASE
                # =====================================================

                save_candidate(

                    name if name else file.name,

                    email,

                    phone,

                    format_education(education),

                    experience,

                    ", ".join(skills),

                    ", ".join(matched),

                    round(final_score, 2),

                    result,

                     resume_path
                    )

                # =====================================
                # SAVE RESULT
                # =====================================

                st.session_state.results.append({

                    "Name":
                    name if name else file.name,

                    "Email":
                    email,

                    "Phone":
                    phone,

                    "Education":
                    format_education(education),

                    "Experience":
                    experience,

                    "Skills":
                    ", ".join(skills),

                    "Matched Skills":
                    ", ".join(matched),

                    "Skill Score":
                    round(skill_score, 2),

                    "JD Score":
                    round(jd_score, 2),

                    "Education Score":
                    round(edu_score, 2),

                    "Experience Score":
                    round(exp_score, 2),

                    "Total Score":
                    round(final_score, 2),

                    "Result":
                    result,

                    "Why Selected":
                    why_selected
                })

            st.success(
                "Resume Analysis Completed!"
            )

    # =================================================
    # SHOW RESULTS
    # =================================================

    if st.session_state.results:

        df = pd.DataFrame(
            st.session_state.results
        )

        ranked_df = df.sort_values(
            by="Total Score",
            ascending=False
        )

        st.subheader(
            "🏆 Candidate Ranking"
        )

        st.dataframe(
            ranked_df,
            use_container_width=True
        )

        # ============================================
        # CSV DOWNLOAD
        # ============================================

        csv = ranked_df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="⬇ Download Results CSV",
            data=csv,
            file_name='resume_screening_results.csv',
            mime='text/csv'
        )

        st.subheader(
            "🎯 Candidate Profiles"
        )

        for _, row in ranked_df.iterrows():

            show_candidate(row)

            with st.expander(
                f"🤖 AI Analysis - {row['Name']}"
            ):

                st.write(row["Why Selected"])

   
# =====================================================
# DASHBOARD
# =====================================================

elif menu == "Dashboard":

    st.header("📊 Dashboard")

    df = pd.DataFrame(
        st.session_state.results
    )

    if df.empty:

        st.info(
            "No resume analysis available."
        )

    else:

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Candidates",
            len(df)
        )

        col2.metric(
            "Selected",
            len(df[df["Result"] == "Selected"])
        )

        col3.metric(
            "Standby",
            len(df[df["Result"] == "Standby"])
        )

        col4.metric(
            "Average Score",
            round(df["Total Score"].mean(), 2)
        )

        st.divider()

        st.dataframe(
            df.sort_values(
                by="Total Score",
                ascending=False
            ),
            use_container_width=True
        )


# =====================================================
# ANALYTICS
# =====================================================

elif menu == "Analytics":

    st.header("📈 Resume Analytics")

    df = pd.DataFrame(
        st.session_state.results
    )

    if df.empty:

        st.info(
            "No analytics available."
        )

    else:

        st.subheader(
            "📊 Score Distribution"
        )

        fig1, ax1 = plt.subplots(
            figsize=(8, 4)
        )

        ax1.hist(df["Total Score"])

        st.pyplot(fig1)

        st.subheader(
            "🧠 Skill Score vs JD Score"
        )

        fig2, ax2 = plt.subplots(
            figsize=(8, 4)
        )

        ax2.scatter(
            df["Skill Score"],
            df["JD Score"]
        )

        st.pyplot(fig2)


# =========================================================
# CHATBOT PAGE
# =========================================================

elif menu == "AI Chatbot":

    st.header("🤖 Recruitment Assistant")

    st.markdown("""
    Ask questions about candidates and resumes.
    
    Example Questions:
    
    🔹 Who is the best candidate?  
    🔹 Why was John selected?  
    🔹 Show rejected candidates  
    🔹 Show skills  
    🔹 Show experience  
    🔹 Highest JD match  
    🔹 Show top 3 candidates  
    🔹 Who has highest experience?  
    🔹 List all candidates  
    🔹 CANDIDATES WITH SPECIFIC SKILL  
    🔹 Who has lowest score?  
    🔹 Show candidate details of John  
    🔹 Which candidate has best education?  
    """)

    # =====================================================
    # CHECK RESULTS
    # =====================================================

    if not st.session_state.results:

        st.warning("Please analyze resumes first.")

    else:

        # =================================================
        # DATAFRAME
        # =================================================

        df = pd.DataFrame(st.session_state.results)

        # =================================================
        # CHAT HISTORY
        # =================================================

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # =================================================
        # USER INPUT
        # =================================================

        user_question = st.text_input(
            "Ask Question",
            placeholder="Example: Who is the best candidate?"
        )

        # =================================================
        # SEND BUTTON
        # =================================================

        if st.button("Send"):

            if user_question:

                question = user_question.lower()

                response = "Sorry, I could not understand the question."

                # =================================================
                # BEST CANDIDATE
                # =================================================

                if "best candidate" in question or "highest score" in question:

                    best = df.sort_values(
                        by="Total Score",
                        ascending=False
                    ).iloc[0]

                    response = f"""
<div style="
background:#0f766e;
padding:20px;
border-radius:15px;
margin-bottom:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🏆 Best Candidate

<br><br>

<b>Name:</b> {best['Name']}<br><br>

<b>Total Score:</b> {best['Total Score']}<br><br>

<b>Skills:</b> {best['Matched Skills']}<br><br>

<b>Result:</b> {best['Result']}

</div>
"""

                # =================================================
                # REJECTED CANDIDATES
                # =================================================

                elif "rejected" in question:

                    rejected_df = df[df["Result"] == "Rejected"]

                    if rejected_df.empty:

                        response = """
<div style="
background:#7c2d12;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
">

No rejected candidates found.

</div>
"""

                    else:

                        names = "<br>".join(rejected_df["Name"].tolist())

                        response = f"""
<div style="
background:#7c2d12;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

❌ Rejected Candidates

<br><br>

{names}

</div>
"""

                # =================================================
                # TOP 3 CANDIDATES
                # =================================================

                elif "top 3" in question:

                    top3 = df.sort_values(
                        by="Total Score",
                        ascending=False
                    ).head(3)

                    rows = ""

                    for _, row in top3.iterrows():

                        rows += f"""
<b>{row['Name']}</b><br>
Score: {row['Total Score']}<br>
Skills: {row['Matched Skills']}<br><br>
"""

                    response = f"""
<div style="
background:#1d4ed8;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🥇 Top 3 Candidates

<br><br>

{rows}

</div>
"""

                # =================================================
                # HIGHEST EXPERIENCE
                # =================================================

                elif "highest experience" in question or "most experienced" in question:

                    top_exp = df.sort_values(
                        by="Experience",
                        ascending=False
                    ).iloc[0]

                    response = f"""
<div style="
background:#0f766e;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

👨‍💼 Most Experienced Candidate

<br><br>

<b>Name:</b> {top_exp['Name']}<br><br>

<b>Experience:</b> {top_exp['Experience']} years<br><br>

<b>Skills:</b> {top_exp['Skills']}

</div>
"""

                # =================================================
                # LOWEST SCORE
                # =================================================

                elif "lowest score" in question:

                    low = df.sort_values(
                        by="Total Score",
                        ascending=True
                    ).iloc[0]

                    response = f"""
<div style="
background:#991b1b;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

📉 Lowest Score Candidate

<br><br>

<b>Name:</b> {low['Name']}<br><br>

<b>Score:</b> {low['Total Score']}

</div>
"""

                # =================================================
                # LIST ALL CANDIDATES
                # =================================================

                elif "list all candidates" in question:

                    candidate_names = "<br>".join(df["Name"].tolist())

                    response = f"""
<div style="
background:#1e3a8a;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

📋 All Candidates

<br><br>

{candidate_names}

</div>
"""

                # =================================================
                # SHOW SKILLS
                # =================================================

                elif "show skills" in question:

                    skills_text = ""

                    for _, row in df.iterrows():

                        skills_text += f"""
<b>{row['Name']}</b><br>
{row['Skills']}<br><br>
"""

                    response = f"""
<div style="
background:#374151;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🛠 Candidate Skills

<br><br>

{skills_text}

</div>
"""

                # =================================================
                # SHOW EXPERIENCE
                # =================================================

                elif "show experience" in question:

                    exp_text = ""

                    for _, row in df.iterrows():

                        exp_text += f"""
<b>{row['Name']}</b><br>
Experience: {row['Experience']} years<br><br>
"""

                    response = f"""
<div style="
background:#065f46;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

📈 Candidate Experience

<br><br>

{exp_text}

</div>
"""

                # =================================================
                # HIGHEST JD MATCH
                # =================================================

                elif "highest jd" in question:

                    jd_top = df.sort_values(
                        by="JD Score",
                        ascending=False
                    ).iloc[0]

                    response = f"""
<div style="
background:#4338ca;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🎯 Highest JD Match

<br><br>

<b>Name:</b> {jd_top['Name']}<br><br>

<b>JD Score:</b> {jd_top['JD Score']}

</div>
"""
                # =================================================
                # WHY WAS CANDIDATE SELECTED
                # =================================================

                elif "why was" in question and "selected" in question:

                    candidate_name = question.replace(
                        "why was",
                        ""
                    ).replace(
                        "selected",
                        ""
                    ).strip()

                    candidate_df = df[
                        df["Name"].str.lower().str.contains(
                            candidate_name
                        )
                    ]

                    if candidate_df.empty:

                        response = f"""
<div style="
background:#991b1b;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
">

Candidate not found.

</div>
"""

                    else:

                        candidate = candidate_df.iloc[0]

                        response = f"""
<div style="
background:#0f766e;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🤖 Why Candidate Was Selected

<br><br>

<b>Name:</b> {candidate['Name']}<br><br>

<b>Matched Skills:</b> {candidate['Matched Skills']}<br><br>

<b>Experience:</b> {candidate['Experience']} years<br><br>

<b>Total Score:</b> {candidate['Total Score']}<br><br>

<b>AI Analysis:</b><br>
{candidate['Why Selected']}

</div>
"""    
                # =================================================
                # CANDIDATE DETAILS
                # =================================================

                elif "candidate details" in question or "details of" in question:

                    candidate_name = question.replace(
                        "show candidate details of",
                        ""
                    ).replace(
                        "details of",
                        ""
                    ).strip()

                    candidate_df = df[
                        df["Name"].str.lower().str.contains(
                            candidate_name
                        )
                    ]

                    if candidate_df.empty:

                        response = """
<div style="
background:#991b1b;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
">

Candidate not found.

</div>
"""

                    else:

                        candidate = candidate_df.iloc[0]

                        response = f"""
<div style="
background:#374151;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

📋 Candidate Details

<br><br>

<b>Name:</b> {candidate['Name']}<br><br>

<b>Email:</b> {candidate['Email']}<br><br>

<b>Phone:</b> {candidate['Phone']}<br><br>

<b>Skills:</b> {candidate['Skills']}<br><br>

<b>Education:</b> {candidate['Education']}<br><br>

<b>Experience:</b> {candidate['Experience']} years<br><br>

<b>Total Score:</b> {candidate['Total Score']}

</div>
"""        
                # =================================================
                # BEST EDUCATION
                # =================================================

                elif "best education" in question:

                    candidate = df.iloc[0]

                    response = f"""
<div style="
background:#4338ca;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🎓 Candidate With Best Education

<br><br>

<b>Name:</b> {candidate['Name']}<br><br>

<b>Education:</b><br>
{candidate['Education']}

</div>
"""    

                # =================================================
                # CANDIDATES WITH SPECIFIC SKILL
                # =================================================

                elif "skill" in question:

                    # ---------------------------------------------
                    # EXTRACT SKILL FROM QUESTION
                    # ---------------------------------------------

                    detected_skill = None

                    for skill in ALL_SKILLS:

                        if skill.lower() in question:

                            detected_skill = skill

                            break

                    # ---------------------------------------------
                    # IF SKILL NOT FOUND
                    # ---------------------------------------------

                    if not detected_skill:

                        response = """
<div style="
background:#991b1b;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
">

Skill not recognized.

</div>
"""

                    else:

                        # -----------------------------------------
                        # FILTER CANDIDATES
                        # -----------------------------------------

                        skill_df = df[
                            df["Skills"].str.contains(
                                detected_skill,
                                case=False,
                                na=False
                            )
                        ]

                        # -----------------------------------------
                        # NO CANDIDATE FOUND
                        # -----------------------------------------

                        if skill_df.empty:

                            response = f"""
<div style="
background:#991b1b;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
">

No candidate found with {detected_skill} skill.

</div>
"""

                        else:

                            names = "<br>".join(
                                skill_df["Name"].tolist()
                            )

                            response = f"""
<div style="
background:#1d4ed8;
padding:20px;
border-radius:15px;
color:white;
font-size:18px;
line-height:1.8;
">

🛠 Candidates With {detected_skill.title()} Skill

<br><br>

{names}

</div>
"""        

                # =================================================
                # STORE CHAT
                # =================================================

                st.session_state.chat_history.append(
                    ("user", user_question)
                )

                st.session_state.chat_history.append(
                    ("bot", response)
                )

        # =================================================
        # SHOW CHAT HISTORY
        # =================================================

        for sender, message in st.session_state.chat_history:

            if sender == "user":

                st.markdown(f"""
<div style="
background:#1e293b;
padding:20px;
border-radius:15px;
margin-bottom:15px;
color:white;
font-size:18px;
line-height:1.8;
">

👩 You
<br><br>
{message}
</div>
""", unsafe_allow_html=True)

            else:

                st.markdown(
                    message,
                    unsafe_allow_html=True
                )

# =====================================================
# MANAGE USERS
# =====================================================

elif menu == "Manage Users":

    st.header("👥 Manage Users")

    import sqlite3

    conn = sqlite3.connect(
        "users.db",
        check_same_thread=False
    )

    users_df = pd.read_sql_query(
        """
        SELECT
        id,
        email,
        role

        FROM users
        """,
        conn
    )

    st.dataframe(
        users_df,
        use_container_width=True
    )

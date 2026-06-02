# #---------------------------------
# import os

# from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# # ==========================================
# # LOAD OPENAI MODEL
# # ==========================================

# try:

#     llm = ChatOpenAI(
#         model="gpt-3.5-turbo",
#         temperature=0.3
#     )

# except:

#     llm = None

# # ==========================================
# # AI REASONING
# # ==========================================

# def ai_reason_selection(resume, jd):

#     # --------------------------------------
#     # FALLBACK IF API NOT AVAILABLE
#     # --------------------------------------

#     if llm is None:

#         return """
# Candidate evaluated using local ATS scoring.

# OpenAI service unavailable.
# """

#     try:

#         prompt = PromptTemplate.from_template("""

# You are an AI recruitment assistant.

# Analyze the resume against the job description.

# Resume:
# {resume}

# Job Description:
# {jd}

# Give:
# 1. Matching skills
# 2. Strengths
# 3. Missing skills
# 4. Hiring recommendation

# Keep response short and professional.

# """)

#         chain = prompt | llm

#         result = chain.invoke({

#             "resume": resume[:3000],

#             "jd": jd[:1500]

#         })

#         return result.content

#     # --------------------------------------
#     # HANDLE QUOTA ERRORS
#     # --------------------------------------

#     except Exception:

#         return """
# AI analysis temporarily unavailable.

# Candidate evaluated using:
# • Skill Matching
# • Education Scoring
# • Experience Scoring
# • JD Similarity
# """






import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# ==========================================
# OPENAI MODEL
# ==========================================

try:

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3
    )

except:

    llm = None

# ==========================================
# LOCAL AI ANALYSIS
# ==========================================

def generate_local_reason(
    matched_skills,
    missing_skills,
    experience,
    score,
    result
):

    strengths = []

    if matched_skills:

        strengths.append(
            f"Matched skills: {', '.join(matched_skills[:5])}"
        )

    if experience >= 2:

        strengths.append(
            f"{experience} years of relevant experience"
        )

    if score >= 75:

        strengths.append(
            "Strong overall ATS score"
        )

    elif score >= 60:

        strengths.append(
            "Moderate ATS performance"
        )

    if missing_skills:

        missing = ", ".join(missing_skills[:5])

        weaknesses = (
            f"Missing skills: {missing}"
        )

    else:

        weaknesses = (
            "Most required skills are matched"
        )

    recommendation = result

    final_reason = f"""

✅ Strengths:
{chr(10).join(['• ' + s for s in strengths])}

⚠ Missing Areas:
• {weaknesses}

📌 Recommendation:
• Candidate classified as: {recommendation}

"""

    return final_reason

# ==========================================
# OPENAI ENHANCEMENT
# ==========================================

def ai_reason_selection(
    resume,
    jd,
    matched_skills,
    missing_skills,
    experience,
    score,
    result
):

    # --------------------------------------
    # ALWAYS GENERATE LOCAL ANALYSIS
    # --------------------------------------

    local_reason = generate_local_reason(
        matched_skills,
        missing_skills,
        experience,
        score,
        result
    )

    # --------------------------------------
    # IF OPENAI NOT AVAILABLE
    # --------------------------------------

    if llm is None:

        return local_reason

    try:

        prompt = PromptTemplate.from_template("""

You are an HR recruitment assistant.

Resume:
{resume}

Job Description:
{jd}

ATS Analysis:
{local_reason}

Improve this ATS analysis into a professional HR evaluation.

Keep it concise and readable.

""")

        chain = prompt | llm

        result_ai = chain.invoke({

            "resume": resume[:3000],

            "jd": jd[:1500],

            "local_reason": local_reason

        })

        return result_ai.content

    except:

        # FALLBACK TO LOCAL AI
        return local_reason


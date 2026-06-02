from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')


# -------------------------------
# NORMALIZE SKILLS
# -------------------------------
def normalize_skills(skills):
    if isinstance(skills, list):
        return [str(s).lower().strip() for s in skills if str(s).strip()]
    return []


# -------------------------------
# MATCH SKILLS
# -------------------------------
def match_skills(candidate_skills, required_skills):
    candidate_skills = normalize_skills(candidate_skills)
    required_skills = normalize_skills(required_skills)

    matched = []

    for req in required_skills:
        for skill in candidate_skills:
            if req in skill or skill in req:
                matched.append(req)
                break

    return list(set(matched))


# -------------------------------
# JD MATCHING
# -------------------------------
def jd_similarity(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0

    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)

    score = util.pytorch_cos_sim(emb1, emb2).item()

    return round(score * 100, 2)


# -------------------------------
# FINAL SCORING (NEW 🔥)
# -------------------------------
def calculate_final_score(jd_score, skill_score, edu_score, exp_score):
    
    # Optional safety: if JD is too low, rely more on skills
    if jd_score < 10:
        jd_score = skill_score

    final_score = (
        0.35 * jd_score +
        0.35 * skill_score +
        0.20 * edu_score +
        0.10 * exp_score
    )

    return round(final_score, 2)
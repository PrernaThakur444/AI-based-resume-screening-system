import pandas as pd
# ======================================================
# SCORING FUNCTION
# ======================================================

def calculate_score(
    matched_skills,
    required_skills,
    education_df,
    experience,
    jd_score
):

    # ======================================================
    # 1. SKILL SCORE → 35%
    # ======================================================

    if required_skills:
        skill_ratio = len(matched_skills) / len(required_skills)
    else:
        skill_ratio = 0

    skill_score = round(skill_ratio * 35, 2)

    # ======================================================
    # 2. EDUCATION SCORE → 20%
    # ======================================================

    edu_score = 0

    try:

        if not education_df.empty:

            clean_values = []

            for val in education_df["Percentage"]:

                try:

                    val_str = str(val).strip()

                    if val_str.lower() == "n/a":
                        continue

                    val_str = val_str.rstrip(".")

                    percentage = float(val_str)

                    if 0 <= percentage <= 100:
                        clean_values.append(percentage)

                except:
                    continue

            if clean_values:

                max_percentage = max(clean_values)

                edu_score = round(
                    (max_percentage / 100) * 20,
                    2
                )

    except:
        edu_score = 0

    # ======================================================
    # 3. EXPERIENCE SCORE → 10%
    # ======================================================

    try:

        exp_score = min(experience / 5, 1) * 10
        exp_score = round(exp_score, 2)

    except:
        exp_score = 0

    # ======================================================
    # 4. JD MATCH SCORE → 35%
    # ======================================================

    try:

        jd_score_weighted = round(
            (jd_score / 100) * 35,
            2
        )

    except:
        jd_score_weighted = 0

    # ======================================================
    # 5. TOTAL SCORE
    # ======================================================

    total_score = round(
        skill_score +
        edu_score +
        exp_score +
        jd_score_weighted,
        2
    )

    return (
        skill_score,
        edu_score,
        exp_score,
        total_score
    )


# ======================================================
# CLASSIFICATION FUNCTION
# ======================================================

def classify(score):

    if score >= 70:
        return "Selected"

    elif score >= 50:
        return "Standby"

    else:
        return "Rejected"


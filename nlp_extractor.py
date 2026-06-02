from pydoc import text
import re
import spacy
import pandas as pd


import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# 🔥 CLEAN TEXT
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(\w+)@\s*(\w+)\s*\.\s*(\w+)', r'\1@\2.\3', text)
    return text


# Predefined skills list
SKILLS_DB = ["python", "sql", "excel", "java", "machine learning", "data analysis"]



# ✅ NAME
def extract_name(text):
    lines = text.split("\n")
    
    for line in lines[:10]:
        line = line.strip()
        
        if (
            len(line.split()) <= 3 and
            line.isupper() and
            "@" not in line and
            not any(char.isdigit() for char in line)
        ):
            return line.title()
    
    return "Not Found"


# ✅ EMAIL
def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(pattern, text)
    return matches[0] if matches else "Not Found"


# ✅ PHONE
def extract_phone(text):
    pattern = r'[6-9]\d{9}'
    matches = re.findall(pattern, text)
    return matches[0] if matches else "Not Found"


# ✅ SKILL EXTRACTION
def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILLS_DB if skill in text]
    return list(set(found_skills))

def extract_education(text):
    import pandas as pd
    import re

    # ---------- SAFE TEXT ----------
    if not isinstance(text, str):
        try:
            text = text.page_content
        except:
            text = str(text)

    text = text.lower()

    # Fix broken decimals
    text = re.sub(r"(\d)\s*\.\s*(\d)", r"\1.\2", text)

    # Split lines
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    results = {}

    # ---------- DEGREE PATTERNS ----------
    degree_patterns = {
        # ---------- SCHOOL ----------
        "10th": r"\b(10th|ssc|matric|matriculation)\b",
        "12th": r"\b(12th|hsc|intermediate|higher secondary)\b",

        # ---------- BACHELORS ----------
        "BCA": r"\bb\.?\s*c\.?\s*a\b|bachelor of computer applications",
        "BBA": r"\bb\.?\s*b\.?\s*a\b|bachelor of business administration",
        "BCom": r"\bb\.?\s*com\b|bachelor of commerce",
        "BA": r"\bb\.?\s*a\b|bachelor of arts",
        "BSc": r"\bb\.?\s*sc\b|bachelor of science",
        "BTech": r"\bb\.?\s*tech\b|\bb\.?\s*e\b|bachelor of technology|bachelor of engineering",

        # ---------- MASTERS ----------
        "MCA": r"\bm\.?\s*c\.?\s*a\b|master of computer applications",
        "MBA": r"\bm\.?\s*b\.?\s*a\b|master of business administration",
        "MCom": r"\bm\.?\s*com\b|master of commerce",
        "MA": r"\bm\.?\s*a\b|master of arts",
        "MSc": r"\bm\.?\s*sc\b|master of science",
        "MTech": r"\bm\.?\s*tech\b|master of technology",

        # ---------- DIPLOMA / EDUCATION ----------
        "PGDCA": r"\bpgdca\b|post graduate diploma in computer applications",
        "BEd": r"\bb\.?\s*ed\b|bachelor of education",
        "JBT": r"\bjbt\b|junior basic training",

        # ---------- HIGHER ----------
        "PhD": r"\b(phd|doctorate)\b"
    }

    # ---------- FUNCTION TO EXTRACT % ----------
    # def get_percentage(line):
    #     perc = re.search(r"([4-9]\d(?:\.\d{1,2})?)\s?%", line)
    #     cgpa = re.search(r"(cgpa|gpa)[^\d]*(\d\.\d{1,2})", line)

    #     if perc:
    #         return float(perc.group(1))

    #     if cgpa:
    #         val = float(cgpa.group(2))
    #         return round((val / 10) * 100, 2)

    #     # standalone CGPA like "7.9"
    #     cgpa2 = re.search(r"\b([5-9]\.\d{1,2})\b", line)
    #     if cgpa2:
    #         val = float(cgpa2.group(1))
    #         return round((val / 10) * 100, 2)

    #     return None

    # # ---------- MAIN LOGIC ----------
    # for i, line in enumerate(lines):

    #     for degree, pattern in degree_patterns.items():

    #         if re.search(pattern, line):

    #             percentage = get_percentage(line)

    #             # 🔥 Look only next 2 lines (strict)
    #             if percentage is None:
    #                 for j in range(1, 3):
    #                     if i + j >= len(lines):
    #                         break

    #                     next_line = lines[i + j]

    #                     # stop if next degree starts
    #                     if any(re.search(pat, next_line) for pat in degree_patterns.values()):
    #                         break

    #                     percentage = get_percentage(next_line)
    #                     if percentage is not None:
    #                         break

    #             if percentage is None:
    #                 percentage = "N/A"
  

    def get_percentage_block(lines, i, degree_patterns):
        import re

        # 🔹 Step 1: current line
        line = lines[i]

        # SAME LINE FIRST (MOST IMPORTANT)
        perc = re.search(r"([4-9]\d(?:\.\d{1,2})?)\s?%", line)
        cgpa = re.search(r"(cgpa|gpa)[^\d]*(\d\.\d{1,2})", line)

        if not cgpa:
            cgpa = re.search(r"\b([5-9]\.\d{1,2})\b", line)

        if perc:
            return float(perc.group(1))

        if cgpa:
            val = float(cgpa.group(len(cgpa.groups())))
            return round((val / 10) * 100, 2)

        # 🔹 Step 2: ONLY next 2 lines (STRICT)
        for j in range(1, 3):

            if i + j >= len(lines):
                break

            next_line = lines[i + j]

            # 🚨 STOP if another degree appears
            if any(re.search(pat, next_line) for pat in degree_patterns.values()):
                break

            perc = re.search(r"([4-9]\d(?:\.\d{1,2})?)\s?%", next_line)
            cgpa = re.search(r"(cgpa|gpa)[^\d]*(\d\.\d{1,2})", next_line)

            if not cgpa:
                cgpa = re.search(r"\b([5-9]\.\d{1,2})\b", next_line)

            if perc:
                return float(perc.group(1))

            if cgpa:
                val = float(cgpa.group(len(cgpa.groups())))
                return round((val / 10) * 100, 2)

            return "N/A"

    for i, line in enumerate(lines):

        for degree, pattern in degree_patterns.items():

            if re.search(pattern, line):

                # ✅ get percentage correctly
                percentage = get_percentage_block(lines, i, degree_patterns)

                # ✅ store result
                if degree not in results:
                    results[degree] = percentage

    # ---------- ORDER ----------
    order = ["10th","12th","BCA","BBA","BCom","BA","BSc","BTech",
             "MCA","MBA","MCom","MA","MSc","MTech",
             "PGDCA","BEd","JBT","PhD"]

    data = []
    for deg in order:
        if deg in results:
            data.append({
                "Qualification": deg,
                "Percentage": results[deg]
            })

    if not data:
        return pd.DataFrame([{
            "Qualification": "Not Found",
            "Percentage": "N/A"
        }])

    return pd.DataFrame(data)
def extract_jd_skills(jd_text):
    import re
    from utils.skill_list import ALL_SKILLS

    jd_text = jd_text.lower()

    jd_skills = []

    for skill in ALL_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, jd_text):
            jd_skills.append(skill)

    return list(set(jd_skills))


def extract_experience(text):
    import re

    if not isinstance(text, str):
        try:
            text = text.page_content
        except:
            text = str(text)

    text = text.lower()

    patterns = [
        r"(\d+)\+?\s*years",
        r"(\d+)\s*yrs",
        r"experience\s*[:\-]?\s*(\d+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return float(match.group(1))

    return 0
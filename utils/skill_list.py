# utils/skill_list.py

SKILLS_DB = {
    
    # ---------------- IT / TECH ----------------
    "IT": [
        "python", "java", "c++", "sql", "mysql",
        "html", "css", "javascript", "react",
        "node.js", "django", "flask",
        "machine learning", "deep learning", "nlp",
        "data analysis", "pandas", "numpy",
        "tensorflow", "keras", "pytorch",
        "git", "docker", "aws"
    ],

    # ---------------- TEACHING ----------------
    # "TEACHER": [
    #     "teaching", "lesson planning", "curriculum development",
    #     "classroom management", "student assessment",
    #     "communication", "mentoring",
    #     "subject knowledge", "blackboard teaching",
    #     "online teaching", "smart class"
    # ],
   
    "TEACHER": [

        "teaching",
        "lesson planning",
        "curriculum development",
        "classroom management",
        "student assessment",
        "mentoring",
        "online teaching",
        "smart class",

        # Commerce
        "accounting",
        "financial accounting",
        "business studies",
        "economics",

        # Science
        "physics",
        "chemistry",
        "mathematics",

        # IT Teaching
        "programming",
        "python",
        "java",
        "sql",

        # Humanities
        "history",
        "political science",
        "geography",
        "psychology"
    ],


    # ---------------- ACCOUNTING ----------------
    "ACCOUNTANT": [
        "accounting", "bookkeeping", "tally",
        "gst", "taxation", "financial reporting",
        "auditing", "balance sheet",
        "income tax", "excel", "quickbooks"
    ],

    # ---------------- HR ----------------
    "HR": [
        "recruitment", "talent acquisition",
        "employee engagement", "payroll",
        "hr policies", "onboarding",
        "training and development",
        "performance management"
    ],

    # ---------------- MARKETING ----------------
    "MARKETING": [
        "digital marketing", "seo", "sem",
        "social media marketing", "content marketing",
        "branding", "email marketing",
        "google ads", "analytics"
    ],

    # ---------------- GENERAL (COMMON SKILLS) ----------------
    "GENERAL": [
        "communication", "teamwork",
        "leadership", "problem solving",
        "time management", "adaptability",
        "critical thinking"
    ]
}

def build_skill_list(SKILLS_DB):
    all_skills = []

    for category in SKILLS_DB.values():
        all_skills.extend(category)

    # Remove duplicates
    return list(set([skill.lower().strip() for skill in all_skills]))


ALL_SKILLS = build_skill_list(SKILLS_DB)
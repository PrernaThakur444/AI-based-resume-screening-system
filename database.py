#--------------------------------------------------------------------------#
import sqlite3

# -------------------------------
# CREATE CONNECTION
# -------------------------------
def create_connection():
    return sqlite3.connect("resume_screening.db")


# -------------------------------
# CREATE TABLES
# -------------------------------
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Candidates Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        experience REAL,
        education TEXT,
        skills TEXT
    )
    """)

    # Results Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score REAL,
        result TEXT,
        matched_skills TEXT
    )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# INSERT DATA
# -------------------------------
def insert_candidate(name, email, phone, experience, education, skills):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO candidates (name, email, phone, experience, education, skills)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, phone, experience, education, skills))

    conn.commit()
    conn.close()


def insert_result(name, score, result, matched_skills):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO results (name, score, result, matched_skills)
    VALUES (?, ?, ?, ?)
    """, (name, score, result, matched_skills))

    conn.commit()
    conn.close()
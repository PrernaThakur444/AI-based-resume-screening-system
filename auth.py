# import streamlit as st

# def login():
#     st.title("Admin Login")

#     # username = st.text_input("Username")
#     # password = st.text_input("Password", type="password")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email == "prerna@gmail.com" and password == "thakur":
#             st.session_state["logged_in"] = True
#             st.success("Login Successful")
#         else:
#             st.error("Invalid Credentials")

# # def logout():
# #     if st.button("Logout"):
# #         st.session_state["logged_in"] = False

# def logout():
#     if st.button("Logout"):
#         st.session_state["logged_in"] = False
#         st.session_state["user_email"] = ""
#         st.rerun()



# # auth.py

# import sqlite3
# import hashlib


# # ==========================================
# # CONNECT DATABASE
# # ==========================================

# conn = sqlite3.connect(
#     "users.db",
#     check_same_thread=False
# )

# cursor = conn.cursor()


# # ==========================================
# # CREATE TABLE
# # ==========================================

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (

#     id INTEGER PRIMARY KEY AUTOINCREMENT,

#     email TEXT UNIQUE,

#     password TEXT
# )
# """)

# conn.commit()


# # ==========================================
# # HASH PASSWORD
# # ==========================================

# def hash_password(password):

#     return hashlib.sha256(
#         password.encode()
#     ).hexdigest()


# # ==========================================
# # SIGNUP USER
# # ==========================================

# def signup_user(email, password):

#     try:

#         hashed_password = hash_password(password)

#         cursor.execute(
#             """
#             INSERT INTO users (email, password)
#             VALUES (?, ?)
#             """,
#             (email, hashed_password)
#         )

#         conn.commit()

#         return True

#     except:

#         return False


# # ==========================================
# # LOGIN USER
# # ==========================================

# def login_user(email, password):

#     hashed_password = hash_password(password)

#     cursor.execute(
#         """
#         SELECT * FROM users
#         WHERE email = ?
#         AND password = ?
#         """,
#         (email, hashed_password)
#     )

#     user = cursor.fetchone()

#     return user


import sqlite3
import hashlib

# =========================================
# DATABASE CONNECTION
# =========================================

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()

# =========================================
# CREATE TABLE
# =========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email TEXT UNIQUE,

    password TEXT,

    role TEXT
)
""")

conn.commit()


# =====================================================
# CREATE CANDIDATES TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    email TEXT,

    phone TEXT,

    education TEXT,

    experience REAL,

    skills TEXT,

    matched_skills TEXT,

    total_score REAL,

    result TEXT,

    resume_path TEXT
)
""")

conn.commit()

# =========================================
# HASH PASSWORD
# =========================================

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()

# =========================================
# SIGNUP USER
# =========================================

def signup_user(email, password, role):

    try:

        hashed_password = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users
            (email, password, role)

            VALUES (?, ?, ?)
            """,
            (
                email,
                hashed_password,
                role
            )
        )

        conn.commit()

        return True

    except:

        return False

# =========================================
# LOGIN USER
# =========================================

def login_user(email, password):

    hashed_password = hash_password(password)

    cursor.execute(
        """
        SELECT * FROM users

        WHERE email=?
        AND password=?
        """,
        (
            email,
            hashed_password
        )
    )

    user = cursor.fetchone()

    return user


# =====================================================
# SAVE CANDIDATE
# =====================================================

def save_candidate(

    name,
    email,
    phone,
    education,
    experience,
    skills,
    matched_skills,
    total_score,
    result,
    resume_path
):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO candidates (

        name,
        email,
        phone,
        education,
        experience,
        skills,
        matched_skills,
        total_score,
        result,
        resume_path

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        name,
        email,
        phone,
        education,
        experience,
        skills,
        matched_skills,
        total_score,
        result,
        resume_path
    ))

    conn.commit()

    conn.close()
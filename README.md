<!-- # 📄 AI Resume Screening System

An AI-powered multi-domain Resume Screening & Applicant Tracking System (ATS) built using Python, Streamlit, NLP, Machine Learning concepts, and OpenAI integration.

The system helps recruiters automatically analyze resumes, extract candidate information, compare resumes with job descriptions, rank candidates, and interact with candidate data using an AI chatbot.

---

# 🚀 Features

# 🔐 Authentication System

## ✅ User Authentication
- User Signup
- User Login
- Email & Password Authentication
- Session Management using Streamlit Session State
- SQLite Database Authentication
- Secure Login Validation

## ✅ Role-Based Access Control

Different access levels added:

- Admin
- HR Manager
- Recruiter

### 🔹 Admin
Can:
- Analyze resumes
- View dashboard
- Access analytics
- Use chatbot
- Manage users
- View all candidate data

### 🔹 HR Manager
Can:
- Analyze resumes
- View dashboard
- Access analytics
- Use chatbot

### 🔹 Recruiter
Can:
- Analyze resumes
- View shortlisted candidates
- Use chatbot

---

# 🚪 Logout Feature

Logout button added to:
- Securely end session
- Clear session state
- Return to login page

---

# 📂 Resume Processing

## ✅ Resume Upload
- Upload multiple PDF resumes
- Automatic resume parsing

## ✅ Resume Information Extraction

The system extracts:
- Candidate Name
- Email
- Phone Number
- Skills
- Education
- Experience

---

# 🧠 AI & NLP Features

## ✅ AI Skill Extraction

Technical skills extracted using:
- NLP
- Regex
- OpenAI API
- Custom Skill Database

### ✅ Improved Skill Filtering
The system now:
- Removes unnecessary words
- Avoids extracting languages unnecessarily
- Prevents unrelated text extraction
- Supports domain-specific skills

---

# 🌍 Multi-Domain Resume Screening

Supports multiple domains:

- IT
- Teaching
- HR
- Marketing
- Accounting
- General Domains

---

# 📌 Smart Domain Detection

The system automatically detects job domain based on Job Description (JD).

Example:
- Python + SQL → IT
- Accounting + Taxation → Accounting
- Teaching + Lesson Planning → Teacher

---

# 📊 Resume Matching System

## ✅ Skill Matching

Matches:
- Resume Skills
- Required Skills
- JD Skills

## ✅ JD Similarity Matching

Uses NLP similarity techniques to compare:
- Resume
- Job Description

## ✅ Education Scoring

Scores candidates based on:
- Qualification
- Percentage

### ✅ Improved Education Formatting
Education section now:
- Removes dataframe confusion
- Displays clean formatted output

Example:

```text
BCA - 78% | MCA - 82%
```

instead of:
```text
0 BCA 78%
1 MCA 82%
```

---

## ✅ Experience Scoring

Scores candidates based on years of experience.

---

# 🏆 Candidate Ranking

Candidates are ranked using:
- Skill Score
- JD Similarity
- Education Score
- Experience Score

Final output:
- Selected
- Standby
- Rejected

---

# 🤖 OpenAI Integration

## ✅ OpenAI API Added

Google Gemini API removed and replaced with:
- OpenAI API

### OpenAI used for:
- Candidate reasoning
- AI explanations
- Resume understanding
- AI candidate evaluation

Example:
- "Candidate has strong Python and SQL skills with relevant experience."

---

# 💬 AI Recruitment Chatbot

A built-in chatbot is added to interact with candidate data.

---

# ✅ Chatbot Features

The chatbot can answer:

- Who is the best candidate?
- Show rejected candidates
- Show top 3 candidates
- Highest JD match
- Who has highest experience?
- Show skills
- Show experience
- Which candidate has best education?
- List all candidates
- Candidate details
- Lowest score candidate
- Candidates with Python skill
- Show shortlisted candidates

---

# 📈 Dashboard & Analytics

## ✅ Dashboard

Displays:
- Total Candidates
- Selected Candidates
- Rejected Candidates
- Average Score
- Top Candidates

---

## ✅ Analytics

Charts included:
- Score Distribution
- Skill Score vs JD Score
- Top Skills Analysis

---

# 📥 CSV Download Feature

Recruiters/Admins can now:
- Download candidate analysis
- Export ranked candidates
- Save results as CSV

Useful for:
- HR reports
- Hiring documentation
- Recruitment tracking

---

# 👥 Manage Users Panel

Admin-only feature added.

Admin can:
- View all users
- Manage recruiter accounts
- Manage HR accounts

---

# 🎨 UI Features

## ✅ Modern UI

Custom Streamlit UI with:
- Dark Theme
- Gradient Buttons
- Responsive Layout
- Candidate Cards
- Styled Tables
- Styled Chatbot
- Styled Authentication Pages

---

# 🛠 Technologies Used

# Frontend
- Streamlit
- HTML
- CSS

# Backend
- Python

# AI / NLP
- OpenAI API
- LangChain
- NLP
- Regex
- Sentence Transformers

# Database
- SQLite

# Data Processing
- Pandas
- NumPy

# Visualization
- Matplotlib

---

# 📁 Project Structure

```bash
AI_Resume_Screening_System/
│
├── app.py
├── ai_engine.py
├── auth.py
├── matcher.py
├── scorer.py
├── nlp_extractor.py
├── resume_parser.py
│
├── components/
│   ├── header.py
│   └── candidate_card.py
│
├── utils/
│   └── skill_list.py
│
├── users.db
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repository-link>
cd AI_Resume_Screening_System
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment:

### Windows
```bash
.venv\Scripts\activate
```

### Linux/Mac
```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 OpenAI API Setup

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- Resume Download
- AI Resume Summarization
- AI Interview Question Generator
- Resume Recommendation Engine
- Email Notifications
- MySQL/PostgreSQL Integration
- Cloud Deployment
- Voice Assistant
- Real-time AI Chatbot
- Video Interview Analysis
- Facial Emotion Detection
- Resume Parsing using OCR
- Multi-language Resume Support

---

# 📷 Screens Included

- Login Page
- Signup Page
- Resume Screening
- Dashboard
- Analytics
- AI Chatbot
- Manage Users Page

---

# 📚 Learning Concepts Used

- NLP
- Regex
- AI APIs
- Machine Learning Concepts
- Streamlit UI
- Authentication
- Role-Based Access
- Session State
- Data Visualization
- ATS Workflow
- Resume Parsing
- AI Candidate Ranking

---

# 👩‍💻 Developed By

Prerna Thakur

---

# ⭐ Project Type

AI + NLP + ATS + Resume Screening + Recruitment Automation System -->










#--------------------------------------#
<!-- # 📄 AI Resume Screening System

An AI-powered multi-domain Resume Screening & Applicant Tracking System (ATS) built using Python, Streamlit, NLP, Machine Learning concepts, and OpenAI integration.

The system helps recruiters automatically analyze resumes, extract candidate information, compare resumes with job descriptions, rank candidates, and interact with candidate data using an AI chatbot.

---

# 🚀 Features

# 🔐 Authentication System

## ✅ User Authentication
- User Signup
- User Login
- Email & Password Authentication
- Session Management using Streamlit Session State
- SQLite Database Authentication
- Secure Login Validation

## ✅ Role-Based Access Control

Different access levels added:

- Admin
- HR Manager
- Recruiter

### 🔹 Admin
Can:
- Analyze resumes
- View dashboard
- Access analytics
- Use chatbot
- Manage users
- Download CSV reports
- View all candidate data

### 🔹 HR Manager
Can:
- Analyze resumes
- View dashboard
- Access analytics
- Use chatbot
- Download CSV reports

### 🔹 Recruiter
Can:
- Analyze resumes
- View shortlisted candidates
- Use chatbot
- Download CSV reports

---

# 🚪 Logout Feature

Logout button added to:
- Securely end session
- Clear session state
- Return to login page

---

# 📂 Resume Processing

## ✅ Resume Upload
- Upload multiple PDF resumes
- Automatic resume parsing
- Multi-resume screening support

## ✅ Resume Information Extraction

The system extracts:
- Candidate Name
- Email
- Phone Number
- Skills
- Education
- Experience

---

# 🧠 AI & NLP Features

## ✅ AI Skill Extraction

Technical skills extracted using:
- NLP
- Regex
- OpenAI API
- Custom Skill Database

### ✅ Improved Skill Filtering
The system now:
- Removes unnecessary words
- Avoids extracting unrelated text
- Prevents invalid skill extraction
- Supports domain-specific skills
- Uses normalized skill matching

---

# 🌍 Multi-Domain Resume Screening

Supports multiple domains:

- IT
- Teaching
- HR
- Marketing
- Accounting
- General Domains

---

# 📌 Smart Domain Detection

The system automatically detects job domain based on Job Description (JD).

Example:
- Python + SQL → IT
- Accounting + Taxation → Accounting
- Teaching + Lesson Planning → Teacher

---

# 📊 Resume Matching System

## ✅ Skill Matching

Matches:
- Resume Skills
- Required Skills
- JD Skills

### ✅ Dynamic Skill Matching
The chatbot can dynamically answer:
- Candidates with Python skill
- Candidates with Java skill
- Candidates with SQL skill
- Candidates with any requested skill

---

## ✅ JD Similarity Matching

Uses NLP similarity techniques to compare:
- Resume
- Job Description

Implemented using:
- Sentence Transformers
- Cosine Similarity

---

## ✅ Education Scoring

Scores candidates based on:
- Qualification
- Percentage

### ✅ Improved Education Formatting

Education section now:
- Removes dataframe confusion
- Displays clean formatted output

Example:

```text
BCA - 78% | MCA - 82%
```

instead of:

```text
0 BCA 78%
1 MCA 82%
```

---

## ✅ Experience Scoring

Scores candidates based on years of experience.

### ✅ Improved Experience Extraction
The system now:
- Extracts numeric years
- Avoids false experience values
- Supports fresher candidates

---

# 🏆 Candidate Ranking

Candidates are ranked using:
- Skill Score
- JD Similarity
- Education Score
- Experience Score

Final output:
- Selected
- Standby
- Rejected

### ✅ Improved Ranking Logic
Ranking now:
- Uses normalized scoring
- Avoids constant results
- Dynamically updates dashboard
- Preserves results across pages

---

# 🤖 OpenAI Integration

## ✅ OpenAI API Added

Google Gemini API removed and replaced with:
- OpenAI API

### OpenAI used for:
- Candidate reasoning
- AI explanations
- Resume understanding
- AI candidate evaluation

Example:
- "Candidate has strong Python and SQL skills with relevant experience."

---

# 💬 AI Recruitment Chatbot

A built-in chatbot is added to interact with candidate data.

---

# ✅ Chatbot Features

The chatbot can answer:

- Who is the best candidate?
- Why was John selected?
- Show rejected candidates
- Show skills
- Show experience
- Highest JD match
- Show top 3 candidates
- Who has highest experience?
- List all candidates
- Show candidates with Python skill
- Show candidates with Java skill
- Show candidates with any skill dynamically
- Who has lowest score?
- Show candidate details of John
- Which candidate has best education?
- Show shortlisted candidates

---

# 🎨 Styled Chatbot UI

Custom chatbot interface added with:
- Styled AI response cards
- Styled user messages
- Dark theme chatbot
- Dynamic response rendering
- Chat history support

### ✅ Chatbot Bug Fixes
Issues fixed:
- Blank chatbot page
- HTML closing tag issue (`</div>`)
- AI service unavailable issue
- Chat history rendering issues

---

# 📈 Dashboard & Analytics

## ✅ Dashboard

Displays:
- Total Candidates
- Selected Candidates
- Rejected Candidates
- Average Score
- Top Candidates

---

## ✅ Analytics

Charts included:
- Score Distribution
- Skill Score vs JD Score
- Top Skills Analysis

---

# 📥 CSV Download Feature

Recruiters/Admins can now:
- Download candidate analysis
- Export ranked candidates
- Save results as CSV

Useful for:
- HR reports
- Hiring documentation
- Recruitment tracking

---

# 👥 Manage Users Panel

Admin-only feature added.

Admin can:
- View all users
- Manage recruiter accounts
- Manage HR accounts

---

# 🧪 Jupyter Notebook Testing Added

Complete testing workflow added in Jupyter Notebook for:

- Resume text extraction
- Name extraction
- Email extraction
- Phone extraction
- Skill extraction
- Education extraction
- Experience extraction
- Skill matching
- JD similarity testing
- Final score calculation

### ✅ Testing Improvements
Issues fixed:
- Education extraction not working
- Matched skills empty issue
- Skill normalization issue
- Indentation errors
- Undefined variable issues
- Score calculation mismatch

---

# 🛠 Error Fixes & Improvements

## ✅ Fixed Issues

### Authentication
- Login not working
- Signup duplicate issue
- Session handling issue

### Resume Processing
- Constant results issue
- Extraction logic issue
- Education formatting issue
- Skill matching issue

### Chatbot
- Blank page issue
- HTML rendering issue
- Missing chatbot responses
- Dynamic skill search issue

### UI
- Sidebar showing before login fixed
- Improved navigation flow
- Styled authentication pages

### Dependencies
- Fixed:
  - matplotlib errors
  - spacy errors
  - fitz/PyMuPDF errors
  - frontend module conflict

---

# 🎨 UI Features

## ✅ Modern UI

Custom Streamlit UI with:
- Dark Theme
- Gradient Buttons
- Responsive Layout
- Candidate Cards
- Styled Tables
- Styled Chatbot
- Styled Authentication Pages

---

# 🛠 Technologies Used

# Frontend
- Streamlit
- HTML
- CSS

# Backend
- Python

# AI / NLP
- OpenAI API
- LangChain
- NLP
- Regex
- Sentence Transformers

# Database
- SQLite

# Data Processing
- Pandas
- NumPy

# Visualization
- Matplotlib

# Resume Parsing
- pdfplumber
- PyMuPDF

---

# 📁 Project Structure

```bash
AI_Resume_Screening_System/
│
├── app.py
├── ai_engine.py
├── auth.py
├── matcher.py
├── scorer.py
├── nlp_extractor.py
├── resume_parser.py
│
├── components/
│   ├── header.py
│   └── candidate_card.py
│
├── utils/
│   └── skill_list.py
│
├── users.db
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repository-link>
cd AI_Resume_Screening_System
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment:

### Windows
```bash
.venv\Scripts\activate
```

### Linux/Mac
```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 OpenAI API Setup

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- Resume Download
- AI Resume Summarization
- AI Interview Question Generator
- Resume Recommendation Engine
- Email Notifications
- MySQL/PostgreSQL Integration
- Cloud Deployment
- Voice Assistant
- Real-time AI Chatbot
- Video Interview Analysis
- Facial Emotion Detection
- Resume Parsing using OCR
- Multi-language Resume Support
- AI Candidate Recommendation
- Interview Scheduling System
- Resume Ranking using LLMs
- AI Hiring Insights Dashboard

---

# 📷 Screens Included

- Login Page
- Signup Page
- Resume Screening
- Dashboard
- Analytics
- AI Chatbot
- Manage Users Page

---

# 📚 Learning Concepts Used

- NLP
- Regex
- AI APIs
- Machine Learning Concepts
- Streamlit UI
- Authentication
- Role-Based Access
- Session State
- Data Visualization
- ATS Workflow
- Resume Parsing
- AI Candidate Ranking
- Sentence Embeddings
- Cosine Similarity
- Chatbot Development

---

# 👩‍💻 Developed By

Prerna Thakur

---

# ⭐ Project Type

AI + NLP + ATS + Resume Screening + Recruitment Automation System

--- -->

<!-- # ✅ Where Changes Were Made In Project

## `app.py`
Added:
- Login/Signup
- Role-based access
- Dashboard
- Analytics
- Chatbot
- CSV download
- Logout button
- Manage Users page

## `nlp_extractor.py`
Added/Improved:
- Skill extraction
- Education extraction
- Experience extraction
- Regex improvements

## `matcher.py`
Added:
- Skill normalization
- Dynamic skill matching
- JD similarity logic

## `scorer.py`
Added:
- Final score calculation
- Ranking logic

## `resume_parser.py`
Added:
- PDF parsing
- Resume text extraction

## `users.db`
Added:
- Authentication database
- User role storage

## `.env`
Added:
- OpenAI API key storage

## Jupyter Notebook
Added:
- Full testing workflow
- Extraction testing
- Scoring testing
- Similarity testing -->




#-------------------------------------
# 📄 AI Resume Screening System

An AI-powered multi-domain Resume Screening & Applicant Tracking System (ATS) built using Python, Streamlit, NLP, Machine Learning concepts, OpenAI integration, SQLite Database, and AI Chatbot functionalities.

The system helps recruiters automatically analyze resumes, extract candidate information, compare resumes with job descriptions, rank candidates, store candidate records permanently, and interact with candidate data using an AI recruitment assistant chatbot.

---

# 🚀 Features

# 🔐 Authentication System

## ✅ User Authentication
- User Signup
- User Login
- Email & Password Authentication
- Session Management using Streamlit Session State
- SQLite Database Authentication
- Secure Login Validation

---

# 👥 Role-Based Access Control (RBAC)

Different access levels added:

- Admin
- HR Manager
- Recruiter

---

## 🔹 Admin Access

Admin can:
- Analyze resumes
- Access dashboard
- Access analytics
- Use AI chatbot
- Manage users
- View all candidate records
- Access database records
- Download CSV reports

---

## 🔹 HR Manager Access

HR Manager can:
- Analyze resumes
- Access dashboard
- Access analytics
- Use AI chatbot
- Download candidate reports

---

## 🔹 Recruiter Access

Recruiter can:
- Analyze resumes
- View shortlisted candidates
- Use AI chatbot
- Download candidate CSV reports

---

# 🚪 Logout Feature

Logout button added for:
- Secure session termination
- Session cleanup
- Returning to login page

---

# 🗄 Database Integration

## ✅ SQLite Database Added

The system now permanently stores:

### Users Table
Stores:
- Email
- Password
- Role

### Candidates Table
Stores:
- Candidate Name
- Email
- Phone
- Skills
- Matched Skills
- Education
- Experience
- Total Score
- Result
- Resume Path

---

# 📂 Resume Storage System

## ✅ Permanent Resume PDF Storage

Uploaded resumes are now stored permanently inside:

```bash
uploads/
```

Example:

```bash
uploads/
├── john_resume.pdf
├── alex_cv.pdf
```

---

# 📂 Resume Processing

# ✅ Resume Upload
- Upload multiple PDF resumes
- Drag-and-drop upload support
- PDF validation
- Multi-resume processing

---

# ✅ Resume Information Extraction

The system extracts:
- Candidate Name
- Email
- Phone Number
- Skills
- Education
- Experience

---

# 🧠 AI & NLP Features

# ✅ AI Skill Extraction

Technical skills extracted using:
- NLP
- Regex
- OpenAI API
- Custom Skill Database

---

# ✅ Improved Skill Filtering

The system now:
- Removes unnecessary words
- Avoids unrelated text extraction
- Detects domain-specific technical skills
- Supports dynamic skill matching

---

# 🌍 Multi-Domain Resume Screening

Supports multiple domains:

- IT
- HR
- Teaching
- Marketing
- Accounting
- Management
- General Domains

---

# 📌 Smart Domain Detection

The system automatically detects the domain based on Job Description (JD).

Examples:
- Python + SQL → IT
- Accounting + Taxation → Accounting
- Recruitment + Hiring → HR
- Lesson Planning → Teaching

---

# 📊 Resume Matching System

# ✅ Skill Matching

Matches:
- Resume Skills
- Required Skills
- Job Description Skills

---

# ✅ Dynamic Skill Detection

Chatbot can now answer:
- Candidates with Python skill
- Candidates with Java skill
- Candidates with SQL skill
- Any dynamically asked skill

Example:

```text
Show candidates with Machine Learning skill
```

---

# ✅ JD Similarity Matching

Uses NLP similarity techniques to compare:
- Resume
- Job Description

---

# ✅ Education Scoring

Scores candidates based on:
- Qualification
- Percentage

---

# ✅ Improved Education Formatting

Education section now displays:

```text
BCA - 78% | MCA - 82%
```

instead of raw dataframe format.

---

# ✅ Experience Scoring

Scores candidates based on years of experience.

---

# 🏆 Candidate Ranking System

Candidates are ranked using:
- Skill Score
- JD Similarity
- Education Score
- Experience Score

Final classifications:
- Selected
- Standby
- Rejected

---

# 🤖 OpenAI Integration

# ✅ OpenAI API Added

Google Gemini integration removed and replaced with:
- OpenAI API

---

# OpenAI Used For

- Candidate reasoning
- Resume understanding
- AI explanations
- Candidate evaluation
- Selection analysis

Example:

```text
Candidate has strong Python and SQL skills with relevant project experience.
```

---

# 💬 AI Recruitment Chatbot

A built-in AI chatbot is integrated into the system.

---

# ✅ Chatbot Features

The chatbot can answer:

- Who is the best candidate?
- Why was John selected?
- Show rejected candidates
- Show shortlisted candidates
- Show top 3 candidates
- Highest JD match
- Who has highest experience?
- List all candidates
- Show skills
- Show experience
- Show candidate details
- Which candidate has best education?
- Show candidate with specific skill
- Lowest score candidate

---

# 📈 Dashboard & Analytics

# ✅ Dashboard

Displays:
- Total Candidates
- Selected Candidates
- Rejected Candidates
- Average Score
- Top Ranked Candidates

---

# ✅ Analytics

Charts included:
- Score Distribution
- Skill Score vs JD Score
- Top Skills Analysis
- Candidate Performance Charts

---

# 📥 CSV Download Feature

Recruiters/Admins can:
- Download candidate analysis
- Export ranked candidates
- Save reports as CSV

Useful for:
- HR reports
- Recruitment tracking
- Hiring documentation

---

# 🗂 Database Viewer

Database page added to:
- View permanently stored candidates
- Access ATS records
- Display candidate database inside Streamlit

---

# 👥 Manage Users Panel

Admin-only feature added.

Admin can:
- View all users
- Manage recruiter accounts
- Manage HR accounts

---

# 🎨 UI Features

# ✅ Modern UI

Custom Streamlit UI with:
- Dark Theme
- Gradient Buttons
- Responsive Layout
- Candidate Cards
- Styled Tables
- Styled Chatbot
- Styled Authentication Pages

---

# 📌 Frontend Features Used

The frontend uses:

- Streamlit
- Custom CSS Injection
- Responsive Containers & Columns
- Interactive DataFrames
- Sidebar Navigation
- Candidate Cards
- AI Chatbot Interface
- Matplotlib Visualizations
- Progress Indicators
- File Uploader Component
- KPI Metrics
- Form Validation
- Download Buttons
- Toast Notifications
- Conditional Rendering
- Gradient Theming

---

# 🛠 Technologies Used

# Frontend
- Streamlit
- HTML
- CSS

---

# Backend
- Python

---

# AI / NLP
- OpenAI API
- NLP
- Regex
- Sentence Transformers
- LangChain Concepts

---

# Database
- SQLite3

---

# Data Processing
- Pandas
- NumPy

---

# Visualization
- Matplotlib

---

# 📁 Project Structure

```bash
AI_Resume_Screening_System/
│
├── uploads/
│
├── app.py
├── ai_engine.py
├── auth.py
├── matcher.py
├── scorer.py
├── nlp_extractor.py
├── resume_parser.py
│
├── components/
│   ├── header.py
│   └── candidate_card.py
│
├── utils/
│   └── skill_list.py
│
├── users.db
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

# 1️⃣ Clone Repository

```bash
git clone <repository-link>
cd AI_Resume_Screening_System
```

---

# 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment:

## Windows

```bash
.venv\Scripts\activate
```

## Linux/Mac

```bash
source .venv/bin/activate
```

---

# 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 OpenAI API Setup

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- Resume Download
- AI Resume Summarization
- AI Interview Question Generator
- Resume Recommendation Engine
- Email Notifications
- MySQL/PostgreSQL Migration
- Cloud Deployment
- Voice Assistant
- Real-time AI Chatbot
- OCR Resume Parsing
- Multi-language Resume Support
- AI Hiring Recommendation System
- Video Interview Analysis
- Facial Emotion Detection

---

# 📷 Screens Included

- Login Page
- Signup Page
- Resume Screening
- Dashboard
- Analytics
- AI Chatbot
- Database Viewer
- Manage Users Page

---

# 📚 Learning Concepts Used

- NLP
- Regex
- AI APIs
- Machine Learning Concepts
- Streamlit UI
- Authentication
- SQLite Database
- Role-Based Access
- Session State
- Data Visualization
- ATS Workflow
- Resume Parsing
- AI Candidate Ranking

---

# 👩‍💻 Developed By

Prerna Thakur

---

# ⭐ Project Type

AI + NLP + ATS + Resume Screening + Recruitment Automation System#
# AI-Powered Skill Gap Analyzer & Intelligent Career Acceleration Agent (SkillGap AI)

> **A Mini-Project submitted in partial fulfilment of the requirements for the award of Bachelor of Engineering in Computer Science and Engineering**  
> **Institution:** K.S. Rangasamy College of Technology, Tiruchengode – 637 215  
> **Authors:** Arunitha A (2403737710422066), Leavin Jackson J (2403737710421023), Pravin K P (2403737710421037)  
> **Supervisor:** Mr. S. Insol Rajasekar, M.Tech.  
> **Head of Department:** Dr. K. Poongodi, M.E., Ph.D.

---

## 📌 Executive Summary

Undergraduate engineering students face severe challenges when transitioning from university curricula to modern corporate technology stacks or competitive global Master's programs. Existing Applicant Tracking Systems (ATS) rely on verbatim keyword matching, while generic LLM chatbots frequently hallucinate admission cutoffs and confusing prerequisites.

**SkillGap AI** solves this through a **hybrid, deterministic-agentic architecture**:
- **Deterministic Mathematical Tools:** 100% precision for CGPA cutoff verification, 2-year total affordability evaluations, and multi-dimensional skill gap quantification.
- **Agentic AI Orchestration:** Google Gemini 2.0 Flash synthesized career counseling, explanation of fit ratings, and personalized 5-month milestone roadmaps.
- **5-Factor Decision Scoring:** Weighted model evaluating Academic Fit (30%), Career Fit (25%), Financial Fit (20%), Skill Fit (15%), and Preference Fit (10%).
- **Objective Categorization:** Automatic classification into **SAFE**, **TARGET**, and **AMBITIOUS** brackets.
- **Interactive What-If Simulation Engine:** Dynamic recalculation of readiness and university categorization in real time as students acquire proficiencies.
- **Zero-Downtime Fallback:** Embedded Node.js deterministic engine guaranteeing 100% platform availability if Python AI microservice is offline.

---

## 🏛️ System Architecture

SkillGap AI is architected across four decoupled layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. PRESENTATION LAYER (React 19 / Vite / Tailwind CSS / Recharts)      │
│    • Student Profile Ingestion     • Real-Time Agent Activity Banner   │
│    • 5-Factor Match Cards          • Interactive What-If Simulator     │
│    • 2-Year Financial Breakdown    • AI Counselor Chatbot Drawer       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ HTTP / REST (JSON)
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. API GATEWAY LAYER (Node.js & Express 4.21, Helmet, CORS)            │
│    • REST Endpoints Routing        • Schema Payload Validation         │
│    • Local Deterministic Engine    • Resilient Fallback Orchestrator   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Internal Proxy (Port 8000)
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. AGENT ORCHESTRATION LAYER (Python FastAPI & LangGraph State Machine)│
│    • MasterAgentOrchestrator       • Eligibility Tool (CGPA/IELTS)     │
│    • Financial Affordability Tool  • Skill Gap Matrix Evaluator        │
│    • Google Gemini 2.0 Flash LLM   • 5-Month Roadmap Synthesizer       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Structured Data & Vectors
┌───────────────────────────────────▼────────────────────────────────────┐
│ 4. KNOWLEDGE & PERSISTENCE LAYER                                       │
│    • Universities Dataset          • Curated Scholarships (DAAD, etc.) │
│    • Role Skill Taxonomies         • PostgreSQL (schema.sql / pgvector)│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📐 Mathematical Formulations

### 1. 5-Factor Weighted Recommendation Formula
$$\text{Overall Match Score} = (0.30 \times \text{Academic Fit}) + (0.25 \times \text{Career Fit}) + (0.20 \times \text{Financial Fit}) + (0.15 \times \text{Skill Fit}) + (0.10 \times \text{Preference Fit})$$

### 2. Institutional Categorization Logic
- **`SAFE`**: Academic Fit $\ge 90\%$ **AND** Financial Fit $\ge 90\%$ *(High admission probability & fully affordable)*
- **`TARGET`**: Academic Fit between $80\%$ and $89\%$, **OR** Financial Fit between $70\%$ and $89\%$ *(Realistic, competitive match)*
- **`AMBITIOUS`**: Academic Fit $< 80\%$ **OR** Financial Fit $< 70\%$ *(Challenging cutoff or budget deficit)*

### 3. Skill Competency Vectors
Evaluated across 5 weighted dimensions:
- **Core Technical Skills (35%):** Python, SQL, Data Structures, Linear Algebra
- **Frameworks & Tooling (25%):** PyTorch, TensorFlow, Scikit-Learn, Transformers
- **Domain Specialization (20%):** Deep Learning, Computer Vision, NLP, MLOps
- **Cloud Tooling & DevOps (10%):** Docker, Kubernetes, AWS/GCP, CI/CD
- **Soft Competencies (10%):** Problem Solving, Technical Writing, Agile

Readiness brackets:
- **`COMPETITIVE MATCH`**: Overall readiness $\ge 85\%$
- **`PARTIAL PROFICIENCY`**: Overall readiness between $65\%$ and $84\%$
- **`CRITICAL GAP`**: Overall readiness $< 65\%$

---

## 📁 Repository Directory Structure

```
AI_Mini_Project/
├── AI_Skill_Gap_Analyzer_Exact_31_Pages.docx  # Original mini-project report
├── package.json                               # Root package configuration
├── schema.sql                                 # PostgreSQL relational schema
├── README.md                                  # Complete documentation
│
├── server/                                    # API Gateway Layer (Port 5000)
│   ├── server.js                              # Express gateway server
│   └── services/
│       └── deterministicAnalyzer.js           # Deterministic analysis engine
│
├── data/                                      # Knowledge Base Datasets
│   ├── universities.json                      # Top European, US, Asian institutions
│   ├── scholarships.json                      # DAAD, Erasmus+, Inlaks, etc.
│   ├── courses.json                           # Specialization curricula
│   └── job_roles.json                         # Benchmark skill taxonomies
│
├── agent/                                     # AI Agent Layer (FastAPI, Port 8000)
│   ├── requirements.txt                       # Python dependencies
│   ├── fastapi_app.py                         # FastAPI microservice
│   ├── master_orchestrator.py                 # LangGraph state machine orchestrator
│   └── tools/
│       ├── __init__.py
│       ├── eligibility_tool.py                # Deterministic CGPA/IELTS checker
│       ├── finance_tool.py                    # 2-Year affordability calculator
│       └── skill_gap_tool.py                  # 5-factor competency vector engine
│
└── client/                                    # Presentation Layer
    ├── package.json                           # React 19 / Vite configuration
    ├── vite.config.js                         # Vite development server
    ├── index.html                             # Vite template
    ├── dist/
    │   └── index.html                         # Production interactive dashboard
    └── src/
        ├── main.jsx                           # React entrypoint
        ├── App.jsx                            # React root component
        └── index.css                          # Tailwind CSS styling
```

---

## 🚀 Quick Start Guide

### Step 1: Install Dependencies
Open PowerShell or Command Prompt in the project folder:
```powershell
npm install
```

### Step 2: Launch the API Gateway & Application
Run:
```powershell
node server/server.js
```
*(Or `npm start`)*

Open your browser and navigate to:
```
http://localhost:5000
```
The full interactive SkillGap AI dashboard is immediately live!

### Step 3 (Optional): Launch Python AI Microservice
To run the specialized Python FastAPI agent on port 8000:
```powershell
cd agent
pip install -r requirements.txt
python fastapi_app.py
```

---

## 🧪 Functional Test Cases & Validation (Chapter 5.2)

| Test ID | Module | Input / Operation | Expected Output | Status |
|:---|:---|:---|:---|:---|
| **TC01** | Backend Health Check | `GET /api/health` | HTTP 200 & Online Status | **Passed** |
| **TC02** | Profile Ingestion | `POST /api/student` | Validates payload & timestamp | **Passed** |
| **TC03** | CGPA Cutoff Evaluation | CGPA 7.2 vs RWTH Aachen (7.5 min) | Status: *Not Eligible* (Missing CGPA) | **Passed** |
| **TC04** | Language Cutoff Check | IELTS 6.0 vs 6.5 Requirement | Status: *Partially Eligible* | **Passed** |
| **TC05** | Affordability Analyzer | Budget ₹15L vs Total Cost ₹17.98L | Status: *EXCEEDS BUDGET* (-₹2.98L) | **Passed** |
| **TC06** | 5-Factor Recommendation | `POST /api/agent/analyze` | Categorized SAFE/TARGET/AMBITIOUS | **Passed** |
| **TC07** | Country Filter Execution | Filter: "Germany" | Targets only German institutions | **Passed** |

---

## 💡 Key Features Implemented

1. **Deterministic Eligibility Tool:** Verifies minimum CGPA, IELTS, TOEFL, and GRE requirements with zero mathematical hallucination.
2. **2-Year Financial Cost Breakdown:** Calculates tuition, living costs, health insurance, and visa expenses, reporting exact budget surplus/deficit.
3. **Multidimensional Competency Diagnostics:** Visualizes readiness %, identifies validated proficiencies, and highlights critical missing gaps.
4. **Interactive What-If Simulation Engine:** Allows students to simulate acquiring skills (e.g. PyTorch, Docker) or increasing CGPA to watch their match score recalibrate instantly.
5. **5-Month Actionable Upskilling Roadmap:** Detailed milestone timeline with capstone repository requirements, LOR commitments, and visa procedures.
6. **AI Counselor Chatbot:** Grounded conversational agent answering admissions, financial, and roadmap questions.
7. **Curated Scholarship Directory:** Quick reference for DAAD, Erasmus Mundus, and national grants.


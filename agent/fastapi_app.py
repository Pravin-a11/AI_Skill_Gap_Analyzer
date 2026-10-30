"""
FastAPI AI Microservice (agent/fastapi_app.py)
Exposes REST endpoints for the AI Agent as specified in Table 4.3.
Ports: 8000 (FastAPI AI Service)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os

from .master_orchestrator import MasterAgentOrchestrator

app = FastAPI(
    title="SkillGap AI - Agent Microservice",
    description="Deterministic skill gap quantification and agentic career planning microservice",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = MasterAgentOrchestrator()

class StudentProfileModel(BaseModel):
    name: str = "Demo Student"
    degree: str = "B.E. Computer Science and Engineering"
    branch: str = "Computer Science"
    cgpa: float = 8.2
    ieltsScore: float = 7.0
    toeflScore: Optional[float] = 0.0
    greScore: Optional[float] = 0.0
    budgetInr: float = 1500000.0
    targetSpecialization: str = "Artificial Intelligence"
    preferredCountry: Optional[str] = "Germany"
    skills: List[str] = ["Python", "Machine Learning", "SQL"]

class ChatRequest(BaseModel):
    message: str
    student_profile: Optional[dict] = None

@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "SkillGap AI Agent Microservice",
        "version": "1.0.0",
        "orchestrator_state": "ready"
    }

@app.post("/agent/analyze")
def analyze_student(profile: StudentProfileModel):
    try:
        results = orchestrator.run_analysis(profile.dict())
        return {
            "success": True,
            "data": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent/what-if")
def what_if_simulation(profile: StudentProfileModel):
    try:
        results = orchestrator.run_analysis(profile.dict())
        return {
            "success": True,
            "simulated_data": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent/chat")
def counselor_chat(req: ChatRequest):
    # Context-grounded empathetic counseling response
    msg = req.message.lower()
    profile = req.student_profile or {}
    cgpa = profile.get("cgpa", 8.2)
    spec = profile.get("targetSpecialization", "Artificial Intelligence")
    country = profile.get("preferredCountry", "Germany")

    if "safe" in msg:
        reply = (
            f"An institution is categorized as SAFE when your academic fit is >= 90% and your financial fit is >= 90%. "
            f"With your CGPA of {cgpa}, RWTH Aachen qualifies as SAFE because its cutoff is 7.5 and tuition is only €600/year, "
            f"making it comfortably within your budget."
        )
    elif "budget" in msg or "money" in msg or "cost" in msg:
        reply = (
            f"For studying in {country}, the largest financial component is the 2-year living cost (approximately €17,000 to €22,000). "
            f"You can offset this through DAAD scholarships (providing €934/month) or by working permitted student part-time jobs (Werkstudent) "
            f"for up to 20 hours per week."
        )
    elif "month" in msg or "roadmap" in msg or "project" in msg:
        reply = (
            f"In Month 1 & 2 of your roadmap, you should focus on building a robust {spec} capstone project incorporating PyTorch and MLOps. "
            f"Ensure you document it with a clean README, modular Python code, unit tests, and deploy a demo on HuggingFace Spaces."
        )
    elif "german" in msg or "language" in msg:
        reply = (
            f"Most English-taught Master's degrees in Germany require only IELTS 6.5 or TOEFL 85. However, learning conversational German (A1/A2 level) "
            f"during Month 1-3 is highly recommended for daily living, visa confidence, and securing local working student positions."
        )
    else:
        reply = (
            f"Hello! I am your SkillGap AI Career Counselor. Based on your profile aiming for {spec} in {country}, "
            f"you have solid fundamentals. You can ask me about university eligibility cutoffs, scholarship applications (like DAAD), "
            f"portfolio projects, or how to bridge specific technical skill gaps!"
        )

    return {
        "reply": reply,
        "role": "SkillGap AI Counselor"
    }

if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000, reload=True)


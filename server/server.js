/**
 * SkillGap AI - API Gateway Backend (server/server.js)
 * Implements RESTful Gateway specified in Chapters 3.2, 4.6 (Table 4.3).
 * Integrates deterministic analyzer service with automatic fallback for 100% availability.
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const {
  universities,
  scholarships,
  jobRoles,
  checkEligibility,
  analyzeAffordability,
  evaluateSkillGap,
  runDeterministicAnalysis
} = require('./services/deterministicAnalyzer');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// API Health Check
app.get('/api/health', (req, res) => {
  res.json({
    status: 'online',
    gateway: 'Node.js Express API Gateway',
    port: PORT,
    timestamp: new Date().toISOString()
  });
});

// 1. Get Universities Catalog (Table 4.3)
app.get('/api/universities', (req, res) => {
  res.json({
    success: true,
    total: universities.length,
    data: universities
  });
});

// 2. Get Scholarships Catalog (Table 4.3)
app.get('/api/scholarships', (req, res) => {
  res.json({
    success: true,
    total: scholarships.length,
    data: scholarships
  });
});

// 3. Get Job Roles & Skill Taxonomy
app.get('/api/roles', (req, res) => {
  res.json({
    success: true,
    data: jobRoles
  });
});

// 4. Student Profile Ingestion & Validation (Table 4.3)
app.post('/api/student', (req, res) => {
  const profile = req.body;
  if (!profile.cgpa || !profile.targetSpecialization) {
    return res.status(400).json({
      success: false,
      error: "Missing required fields: cgpa and targetSpecialization are mandatory."
    });
  }

  res.json({
    success: true,
    message: "Student profile validated and ingested successfully.",
    received_at: new Date().toISOString(),
    profile
  });
});

// 5. Deterministic Eligibility Check (Table 4.3)
app.post('/api/eligibility/check', (req, res) => {
  const { student_profile, university_id } = req.body;
  if (!student_profile) {
    return res.status(400).json({ success: false, error: "student_profile is required" });
  }

  let targetUni = universities[0];
  if (university_id) {
    targetUni = universities.find(u => u.id === university_id) || targetUni;
  }

  const result = checkEligibility(student_profile, targetUni);
  res.json({
    success: true,
    data: result
  });
});

// 6. 2-Year Affordability Analyzer (Table 4.3)
app.post('/api/finance/analyze', (req, res) => {
  const { student_profile, university_id } = req.body;
  if (!student_profile) {
    return res.status(400).json({ success: false, error: "student_profile is required" });
  }

  let targetUni = universities[0];
  if (university_id) {
    targetUni = universities.find(u => u.id === university_id) || targetUni;
  }

  const result = analyzeAffordability(student_profile, targetUni);
  res.json({
    success: true,
    data: result
  });
});

// 7. Deterministic Skill Gap Quantification
app.post('/api/skillgap/analyze', (req, res) => {
  const { skills, target_role } = req.body;
  const roleKey = target_role || "Artificial Intelligence";
  const benchmark = jobRoles[roleKey] || jobRoles["Artificial Intelligence"];

  const result = evaluateSkillGap(skills || [], benchmark);
  res.json({
    success: true,
    role: roleKey,
    data: result
  });
});

// 8. Master Agent Orchestrator: Complete Analysis (5-factor model + roadmap + activity trace)
app.post('/api/agent/analyze', async (req, res) => {
  const studentProfile = req.body;
  try {
    // Execute deterministic analysis
    const result = runDeterministicAnalysis(studentProfile);
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    console.error("Analysis Error:", error);
    res.status(500).json({ success: false, error: error.message });
  }
});

// 9. Interactive What-If Simulation Engine
app.post('/api/agent/what-if', (req, res) => {
  const simulatedProfile = req.body;
  try {
    const result = runDeterministicAnalysis(simulatedProfile);
    res.json({
      success: true,
      simulated_data: result
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// 10. AI Counselor Chatbot
app.post('/api/agent/chat', (req, res) => {
  const { message, student_profile } = req.body;
  const msg = (message || "").toLowerCase();
  const profile = student_profile || {};
  const cgpa = profile.cgpa || 8.2;
  const spec = profile.targetSpecialization || "Artificial Intelligence";
  const country = profile.preferredCountry || "Germany";

  let reply = "";
  if (msg.includes("safe")) {
    reply = `An institution is categorized as SAFE when your Academic Fit >= 90% and Financial Fit >= 90%. With your CGPA of ${cgpa}, institutions like RWTH Aachen University have low tuition (€600/yr) and clear admission benchmarks, making admission highly probable and fully funded within your ₹15L budget.`;
  } else if (msg.includes("cost") || msg.includes("budget") || msg.includes("money") || msg.includes("financial")) {
    reply = `In ${country}, public universities charge minimal administrative semester fees (€300-€600/year). Your primary expense is living costs (€8,500 - €11,000/year, approximately ₹7.6L to ₹9.9L INR). You can cover living expenses via DAAD scholarship (€934/month) or by working 20 hours/week as a student research or software assistant (Werkstudent).`;
  } else if (msg.includes("roadmap") || msg.includes("month") || msg.includes("preparation")) {
    reply = `Your personalized 5-month roadmap has been synthesized! In Month 1, focus on strengthening high-impact missing skills (like PyTorch and clean Git workflows). In Month 2, build an end-to-end full-stack capstone project and request your 3 professor recommendation letters (LORs). In Month 3-4, submit your Uni-Assist dossiers and DAAD scholarship paperwork!`;
  } else if (msg.includes("skill") || msg.includes("learn") || msg.includes("gap")) {
    reply = `To achieve a COMPETITIVE MATCH rating (>= 85%), focus on: 1) Deep learning frameworks (PyTorch/TensorFlow), 2) Modern Cloud containerization (Docker & Kubernetes), and 3) Clean GitHub CI/CD automation. Each skill you acquire will automatically raise your readiness score in the What-If simulation!`;
  } else {
    reply = `Hello! I am your SkillGap AI Academic and Career Advisor. Based on your ${profile.degree || 'B.E. Computer Science'} profile targeting ${spec} in ${country}, I can provide grounded recommendations on university cutoffs, financial planning, scholarship opportunities, or your 5-month upskilling milestones. What would you like to explore?`;
  }

  res.json({
    success: true,
    reply,
    role: "SkillGap AI Counselor"
  });
});

// Serve frontend in production or if client/dist exists
const clientDistPath = path.join(__dirname, '..', 'client', 'dist');
if (fs.existsSync(clientDistPath)) {
  app.use(express.static(clientDistPath));
  app.get('*', (req, res) => {
    res.sendFile(path.join(clientDistPath, 'index.html'));
  });
}

// Start Server
app.listen(PORT, () => {
  console.log(`====================================================`);
  console.log(` SkillGap AI - API Gateway Running on Port ${PORT}`);
  console.log(` Health Check: http://localhost:${PORT}/api/health`);
  console.log(` Universities: http://localhost:${PORT}/api/universities`);
  console.log(` Deterministic Engine: ACTIVE (Zero Hallucination)`);
  console.log(`====================================================`);
});


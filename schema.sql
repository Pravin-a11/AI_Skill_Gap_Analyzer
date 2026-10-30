-- SkillGap AI: Relational PostgreSQL Schema with pgvector capabilities
-- Defined as specified in AI Mini Project Report (Chapter 4.2)

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- CREATE EXTENSION IF NOT EXISTS vector; -- for pgvector semantic skill embeddings

-- 1. Students Table
CREATE TABLE IF NOT EXISTS students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    degree VARCHAR(100) NOT NULL,
    branch VARCHAR(100) NOT NULL,
    cgpa NUMERIC(4, 2) NOT NULL,
    ielts_score NUMERIC(3, 1),
    toefl_score INTEGER,
    gre_score INTEGER,
    budget_inr NUMERIC(12, 2) NOT NULL,
    target_specialization VARCHAR(100) NOT NULL,
    preferred_country VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Universities Table
CREATE TABLE IF NOT EXISTS universities (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    qs_ranking INTEGER NOT NULL,
    annual_tuition_eur NUMERIC(10, 2) NOT NULL,
    annual_living_eur NUMERIC(10, 2) NOT NULL,
    min_cgpa NUMERIC(4, 2) NOT NULL,
    ielts_min NUMERIC(3, 1) NOT NULL,
    toefl_min INTEGER NOT NULL,
    gre_required BOOLEAN DEFAULT FALSE,
    type VARCHAR(20) NOT NULL,
    acceptance_rate VARCHAR(10),
    website VARCHAR(255)
);

-- 3. Student Assessment & Recommendation Logs
CREATE TABLE IF NOT EXISTS assessments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    university_id VARCHAR(50) REFERENCES universities(id),
    match_score NUMERIC(5, 2) NOT NULL,
    academic_fit NUMERIC(5, 2) NOT NULL,
    career_fit NUMERIC(5, 2) NOT NULL,
    financial_fit NUMERIC(5, 2) NOT NULL,
    skill_fit NUMERIC(5, 2) NOT NULL,
    preference_fit NUMERIC(5, 2) NOT NULL,
    category VARCHAR(20) NOT NULL CHECK (category IN ('SAFE', 'TARGET', 'AMBITIOUS')),
    eligibility_status VARCHAR(20) NOT NULL CHECK (eligibility_status IN ('Eligible', 'Partially Eligible', 'Not Eligible')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Skill Gap Assessments
CREATE TABLE IF NOT EXISTS skill_gap_assessments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    target_role VARCHAR(100) NOT NULL,
    overall_readiness NUMERIC(5, 2) NOT NULL,
    readiness_bracket VARCHAR(30) NOT NULL CHECK (readiness_bracket IN ('COMPETITIVE MATCH', 'PARTIAL PROFICIENCY', 'CRITICAL GAP')),
    matched_skills TEXT[],
    missing_skills TEXT[],
    assessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


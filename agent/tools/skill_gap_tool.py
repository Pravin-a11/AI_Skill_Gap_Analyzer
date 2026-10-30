"""
Skill Gap & Competency Evaluation Tool (agent/tools/skill_gap_tool.py)
Evaluates candidate competencies across 5 weighted dimensions:
- Core Technical Skills (35%)
- Framework & Tooling (25%)
- Domain Knowledge (20%)
- Experience Depth / Cloud Tooling (10%)
- Soft Competencies (10%)
Categorizes candidate readiness into:
- COMPETITIVE MATCH (>= 85%)
- PARTIAL PROFICIENCY (65% - 84%)
- CRITICAL GAP (< 65%)
"""

DEFAULT_BENCHMARK = {
    "coreSkills": ["Python", "Algorithms & Data Structures", "Linear Algebra & Statistics", "SQL"],
    "frameworks": ["PyTorch", "TensorFlow", "Scikit-Learn", "HuggingFace Transformers"],
    "domainKnowledge": ["Deep Learning", "Computer Vision", "Natural Language Processing (NLP)", "MLOps"],
    "cloudDevOps": ["Docker", "Kubernetes", "AWS / GCP", "Git & CI/CD"],
    "softSkills": ["Problem Solving", "Research Paper Writing", "Technical Communication", "Agile Collaboration"]
}

WEIGHTS = {
    "coreSkills": 0.35,
    "frameworks": 0.25,
    "domainKnowledge": 0.20,
    "cloudDevOps": 0.10,
    "softSkills": 0.10
}

def normalize_skill(skill: str) -> str:
    s = skill.strip().lower()
    mapping = {
        "k8s": "Kubernetes",
        "kube": "Kubernetes",
        "py": "Python",
        "ml": "Machine Learning",
        "deep learning": "Deep Learning",
        "nlp": "Natural Language Processing (NLP)",
        "cv": "Computer Vision",
        "tf": "TensorFlow",
        "aws": "AWS / GCP",
        "gcp": "AWS / GCP",
        "git": "Git & CI/CD",
        "cicd": "Git & CI/CD",
        "ci/cd": "Git & CI/CD"
    }
    return mapping.get(s, skill.strip())

def evaluate_skill_gap(candidate_skills: list, role_benchmark: dict = None) -> dict:
    if not role_benchmark:
        benchmark = DEFAULT_BENCHMARK
    else:
        benchmark = role_benchmark.get("categories", DEFAULT_BENCHMARK)

    normalized_candidate = {normalize_skill(s).lower() for s in candidate_skills}

    category_results = {}
    total_score = 0.0
    all_matched = []
    all_missing = []

    for cat, benchmark_skills in benchmark.items():
        weight = WEIGHTS.get(cat, 0.20)
        matched = []
        missing = []

        for b_skill in benchmark_skills:
            if normalize_skill(b_skill).lower() in normalized_candidate or any(normalize_skill(b_skill).lower() in s for s in normalized_candidate):
                matched.append(b_skill)
            else:
                missing.append(b_skill)

        cat_ratio = len(matched) / len(benchmark_skills) if benchmark_skills else 1.0
        cat_score = cat_ratio * 100.0
        weighted_cat_score = cat_score * weight
        total_score += weighted_cat_score

        category_results[cat] = {
            "weight": weight,
            "matched": matched,
            "missing": missing,
            "score": round(cat_score, 1),
            "total_benchmark": len(benchmark_skills),
            "matched_count": len(matched)
        }
        all_matched.extend(matched)
        all_missing.extend(missing)

    overall_readiness = round(total_score, 1)

    if overall_readiness >= 85.0:
        readiness_bracket = "COMPETITIVE MATCH"
    elif overall_readiness >= 65.0:
        readiness_bracket = "PARTIAL PROFICIENCY"
    else:
        readiness_bracket = "CRITICAL GAP"

    return {
        "overall_readiness": overall_readiness,
        "readiness_bracket": readiness_bracket,
        "category_results": category_results,
        "matched_skills": all_matched,
        "missing_skills": all_missing
    }

if __name__ == "__main__":
    sample_skills = ["Python", "SQL", "Machine Learning", "Git"]
    print(evaluate_skill_gap(sample_skills))


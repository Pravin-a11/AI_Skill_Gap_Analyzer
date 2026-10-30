"""
Deterministic Eligibility Tool (agent/tools/eligibility_tool.py)
Implements 100% arithmetic precision for CGPA and standardized test score cutoffs.
As specified in Chapter 8.1.1 and Module 2.
"""

def check_eligibility(student_profile: dict, university: dict) -> dict:
    cgpa = float(student_profile.get("cgpa", 8.2))
    ielts = float(student_profile.get("ieltsScore", 7.0))
    toefl = float(student_profile.get("toeflScore", 0))
    gre = float(student_profile.get("greScore", 0))

    min_cgpa = float(university.get("minCgpa", 7.0))
    min_ielts = float(university.get("ieltsMin", 6.5))
    min_toefl = float(university.get("toeflMin", 80))
    gre_req = university.get("greRequired", False)

    missing = []
    if cgpa < min_cgpa:
        missing.append(f"CGPA {cgpa} is below university cutoff of {min_cgpa}")

    english_pass = (ielts >= min_ielts) or (toefl >= min_toefl)
    if not english_pass:
        missing.append(f"English test score below requirement (IELTS {min_ielts} / TOEFL {min_toefl})")

    if gre_req and gre < 300:
        missing.append(f"GRE score {gre} below recommended threshold of 300")

    if not missing:
        status = "Eligible"
    elif len(missing) == 1 and cgpa >= min_cgpa:
        status = "Partially Eligible"
    else:
        status = "Not Eligible"

    # Compute academic fit percentage
    academic_fit = min(100.0, (cgpa / min_cgpa) * 90.0 if min_cgpa > 0 else 90.0)
    if english_pass:
        academic_fit = min(100.0, academic_fit + 10.0)

    return {
        "university": university.get("name"),
        "status": status,
        "academic_fit": round(academic_fit, 1),
        "missing_requirements": missing,
        "is_eligible": status != "Not Eligible"
    }

if __name__ == "__main__":
    sample_student = {"cgpa": 8.2, "ieltsScore": 7.0, "toeflScore": 0, "greScore": 0}
    sample_uni = {"name": "RWTH Aachen", "minCgpa": 7.5, "ieltsMin": 6.5, "toeflMin": 85, "greRequired": False}
    print(check_eligibility(sample_student, sample_uni))


"""
Financial Affordability Analyzer (agent/tools/finance_tool.py)
Calculates complete 2-year cost of education (tuition, living, insurance, visa fees)
and evaluates budget surplus or deficit with deterministic accuracy.
As specified in Chapter 3.5 (Module 3) & Chapter 4.7.
"""

EUR_TO_INR = 90.0
HEALTH_INSURANCE_ANNUAL_EUR = 1200.0
VISA_TRAVEL_FLAT_INR = 150000.0

def analyze_affordability(student_profile: dict, university: dict) -> dict:
    budget_inr = float(student_profile.get("budgetInr", 1500000))
    annual_tuition_eur = float(university.get("annualTuitionEur", 600))
    annual_living_eur = float(university.get("annualLivingEur", 8500))

    # 2-Year Totals
    two_year_tuition_eur = annual_tuition_eur * 2
    two_year_living_eur = annual_living_eur * 2
    two_year_insurance_eur = HEALTH_INSURANCE_ANNUAL_EUR * 2

    two_year_tuition_inr = two_year_tuition_eur * EUR_TO_INR
    two_year_living_inr = two_year_living_eur * EUR_TO_INR
    two_year_insurance_inr = two_year_insurance_eur * EUR_TO_INR

    total_2year_cost_inr = (
        two_year_tuition_inr + 
        two_year_living_inr + 
        two_year_insurance_inr + 
        VISA_TRAVEL_FLAT_INR
    )

    difference_inr = budget_inr - total_2year_cost_inr
    is_affordable = difference_inr >= 0

    if is_affordable:
        status = "WITHIN BUDGET"
        financial_fit = min(100.0, 90.0 + (difference_inr / budget_inr) * 10.0)
    else:
        status = "EXCEEDS BUDGET"
        deficit_pct = abs(difference_inr) / total_2year_cost_inr
        financial_fit = max(10.0, 90.0 - (deficit_pct * 100.0))

    return {
        "university": university.get("name"),
        "budget_inr": budget_inr,
        "total_2year_cost_inr": round(total_2year_cost_inr, 2),
        "difference_inr": round(difference_inr, 2),
        "status": status,
        "financial_fit": round(financial_fit, 1),
        "is_affordable": is_affordable,
        "breakdown": {
            "tuition_inr": round(two_year_tuition_inr, 2),
            "living_inr": round(two_year_living_inr, 2),
            "insurance_inr": round(two_year_insurance_inr, 2),
            "visa_travel_inr": round(VISA_TRAVEL_FLAT_INR, 2)
        }
    }

if __name__ == "__main__":
    sample_student = {"budgetInr": 1500000}
    sample_uni = {"name": "RWTH Aachen", "annualTuitionEur": 600, "annualLivingEur": 8500}
    print(analyze_affordability(sample_student, sample_uni))


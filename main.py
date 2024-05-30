import streamlit as st

# Title and description
st.title("Gail Model Breast Cancer Risk Calculator")
st.write("""
### Welcome to the Gail Model Breast Cancer Risk Calculator
This application estimates a woman's 5-year and lifetime risk of developing breast cancer using the Gail Model. 
Fill in the required information to get your risk assessment.
""")

# User inputs
age = st.number_input("Age", min_value=20, max_value=120, value=40)
menarche_age = st.number_input("Age at first menstrual period", min_value=8, max_value=20, value=12)
first_live_birth_age = st.number_input("Age at first live birth", min_value=10, max_value=50, value=25)
num_first_degree_relatives = st.number_input("Number of first-degree relatives with breast cancer", min_value=0, max_value=10, value=0)
num_biopsies = st.number_input("Number of breast biopsies", min_value=0, max_value=10, value=0)
biopsy_with_hyperplasia = st.radio("Any breast biopsy with atypical hyperplasia?", ("No", "Yes"))
race_ethnicity = st.selectbox("Race/Ethnicity", ("White", "African American", "Hispanic", "Asian or Pacific Islander", "American Indian or Alaska Native"))

# Gail Model calculation logic
def calculate_gail_risk(age, menarche_age, first_live_birth_age, num_first_degree_relatives, num_biopsies, biopsy_with_hyperplasia, race_ethnicity):
    # Simplified risk calculation (for illustrative purposes)
    base_risk = 0.02  # Base risk for average population
    risk_factor = 1.0

    # Adjust risk factor based on inputs
    if age >= 50:
        risk_factor *= 1.2
    if menarche_age < 12:
        risk_factor *= 1.1
    if first_live_birth_age > 30:
        risk_factor *= 1.3
    if num_first_degree_relatives >= 1:
        risk_factor *= 1.5
    if num_biopsies >= 1:
        risk_factor *= 1.2
    if biopsy_with_hyperplasia == "Yes":
        risk_factor *= 1.5
    if race_ethnicity == "African American":
        risk_factor *= 0.8  # Example adjustment for different race/ethnicity

    # Calculate 5-year and lifetime risk
    risk_5_year = base_risk * risk_factor
    lifetime_risk = risk_5_year * 5 * (80 - age) / 60  # Simplified estimation

    return risk_5_year, lifetime_risk

# Calculate and display risk
risk_5_year, lifetime_risk = calculate_gail_risk(age, menarche_age, first_live_birth_age, num_first_degree_relatives, num_biopsies, biopsy_with_hyperplasia, race_ethnicity)
st.subheader(f"5-Year Risk: {risk_5_year:.2%}")
st.subheader(f"Lifetime Risk: {lifetime_risk:.2%}")


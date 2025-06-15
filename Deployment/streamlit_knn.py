import streamlit as st
import pandas as pd
import joblib

st.title("Hiring Needs Prediction - KNN Model")

# Input fields
age = st.sidebar.number_input("Age", min_value=18, max_value=65, value=30)
distance = st.sidebar.number_input("Distance From Home (km)")
income = st.sidebar.number_input("Monthly Income")
companies = st.sidebar.number_input("Number of Companies Worked")
total_years = st.sidebar.number_input("Total Working Years")
years_at_company = st.sidebar.number_input("Years at Company")

# Create input DataFrame
input_df = pd.DataFrame([{
    'Age': age,
    'DistanceFromHome': distance,
    'MonthlyIncome': income,
    'NumCompaniesWorked': companies,
    'TotalWorkingYears': total_years,
    'YearsAtCompany': years_at_company
}])

# Load KNN model
model = joblib.load("knn.pkl")

if st.button("Predict Hiring Need"):
    result = model.predict(input_df)[0]
    st.success("High Hiring Need" if result == 1 else "Low Hiring Need")

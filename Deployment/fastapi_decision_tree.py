from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()
model = joblib.load("Decision_Tree.pkl")

class HiringInput(BaseModel):
    Age: float
    DistanceFromHome: float
    MonthlyIncome: float
    NumCompaniesWorked: float
    TotalWorkingYears: float
    YearsAtCompany: float

@app.post("/predict")
def predict(input_data: HiringInput):
    df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(df)[0]
    return {"prediction": "High Hiring Need" if prediction == 1 else "Low Hiring Need"}

from flask import Flask, request, render_template_string
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("Decision_Tree.pkl")

HTML = '''
<h2>Hiring Needs Prediction (Decision Tree)</h2>
<form method="post">
  Age: <input name="age"><br>
  Distance From Home: <input name="distance"><br>
  Monthly Income: <input name="income"><br>
  Num Companies Worked: <input name="companies"><br>
  Total Working Years: <input name="total_years"><br>
  Years at Company: <input name="years_at_company"><br>
  <input type="submit">
</form>
<h3>{{ prediction }}</h3>
'''

@app.route('/', methods=["GET", "POST"])
def predict():
    prediction = ""
    if request.method == "POST":
        data = pd.DataFrame([{
            'Age': float(request.form['age']),
            'DistanceFromHome': float(request.form['distance']),
            'MonthlyIncome': float(request.form['income']),
            'NumCompaniesWorked': float(request.form['companies']),
            'TotalWorkingYears': float(request.form['total_years']),
            'YearsAtCompany': float(request.form['years_at_company'])
        }])
        result = model.predict(data)[0]
        prediction = "High Hiring Need" if result == 1 else "Low Hiring Need"
    return render_template_string(HTML, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

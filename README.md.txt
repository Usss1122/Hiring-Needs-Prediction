 🧑‍💼 Hiring Needs Prediction using Machine Learning

This project predicts employee hiring requirements using HR datasets and multiple ML models. It is designed to support workforce planning and help businesses anticipate future hiring demands.

 📌 Project Highlights

- ✅ Models Implemented: Logistic Regression, SVM, KNN, Naive Bayes, Decision Tree
- ✅ Deployment Interfaces: Streamlit, Flask, FastAPI
- 📊 Evaluation Metrics: Accuracy, Precision, Recall, F1-Score
- 📁 Dataset: Based on HR analytics (IBM, Arkansas DOT, Recruitment Data, etc.) 
🧠 What’s Inside?

📦 Hiring-Needs-Prediction/
 ┣ 📁 models/                 ← Trained `.pkl` model files
 ┣ 📁 deployment/             ← Streamlit, Flask, and FastAPI code
 ┣ 📁 notebooks/              ← Jupyter notebooks with EDA & training
 ┣ 📁 data/                   ← Dataset files or reference link
 ┣ 📁 report/                 ← Final report (.docx or PDF)
 ┣ 📄 requirements.txt        ← Required Python libraries
 ┣ 📄 README.md               ← You're reading it!

🚀 Deployment

 ▶️ Streamlit

streamlit run streamlit_knn.py


### 🌐 Flask
```
python flask_knn.py
 Visit http://127.0.0.1:5000

 ⚡ FastAPI

uvicorn fastapi_knn:app --reload
 Visit http://127.0.0.1:8000/docs


 📊 Model Performance Summary

| Model              | Accuracy | Precision | Recall | F1-Score | Dataset                |
|-------------------|----------|-----------|--------|----------|-------------------------|
| KNN               | 84%      | 82%       | 81%    | 81.5%    | IBM HR Analytics        |
| Decision Tree     | 91%      | 89%       | 90%    | 89.5%    | HR Analytics Dataset    |
| SVM               | 88%      | 86%       | 85%    | 85.5%    | Recruitment Dataset     |
| Naive Bayes       | 79%      | 77%       | 76%    | 76.5%    | Arkansas DOT data       |
| Logistic Regression | 76%    | 74%       | 73%    | 73.5%    | 1,238 data points       |

 🙋‍♀️ Author

Uswa
Final Semester ML Project  
Feel free to fork, contribute, or explore further!
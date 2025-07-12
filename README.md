# 🚀 CodeDetect - ML Powered Web App

A Django web application that intelligently identifies the programming language of a given code snippet using a machine learning model. This application is designed to be lightweight and stateless, primarily focusing on the prediction functionality and **does not require a separate database**.



## ✨ Features

- **Real-time Detection**: Get instant predictions of programming languages as soon as you paste the code.
- **Confidence-Based Results**: 
  - If the model is highly confident, it returns a single language.
  - Otherwise, it displays the **top 3 most probable programming languages** with their confidence scores.
- **User-Friendly Interface**: Clean and responsive web form to paste code and view results.
- **No Database Required**: Lightweight, stateless app that avoids unnecessary complexity.
- **Scalable & Extendable**: Built with Django, making it easy to deploy, scale, or connect to other services.



## 🛠️ Technologies Used

### Backend:
- Python 3.x
- Django
- Scikit-learn (TF-IDF + LogisticRegression, RandomForestClassifier, MultinomialNB)
- Joblib (for model persistence)
- NumPy (for vector math)

### Frontend:
- HTML5
- CSS3
- JavaScript (ES6+)



## 🧠 How It Works

1. **User submits code** via a form on the web interface.
2. **AJAX request** sends the snippet to the Django backend.
3. **ML model** (loaded from `lang_detect_model.joblib`) predicts the probabilities of different programming languages using `predict_proba()`.
4. Based on prediction confidence:
   - If confidence is high, show **only the top language**.
   - If confidence is moderate, return **Top 3 predictions with probabilities**.
   - If confidence is too low, return `"Unknown"` to indicate insufficient syntax match.
5. **JSON response** updates the results area with the prediction output.



## 🧾 Example Output Scenarios

### High Confidence
> **Detected Language:** Python  

### Moderate Confidence
> **Top Predictions:**  
> 1. Python 
> 2. Julia  
> 3. Scala

### Low Confidence / Invalid Input
> **Detected Language:** Invalid or Unknown  
> Reason: Prediction confidence is too low or input syntax is unclear.



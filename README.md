# 🚀 CodeDetect - ML Powered Web App

A Django web application that intelligently identifies the programming language of a given code snippet using a machine learning model. This application is designed to be lightweight and stateless, primarily focusing on the prediction functionality and **does not require a separate vectorizer or a database**.


## ✨ Features

- **Real-time Detection**: Get instant predictions of programming languages.
- **Confidence-Based Results**: Displays either a single highly confident prediction or the top 3 most probable languages with their confidence scores.
- **User-Friendly Interface**: Simple web form for pasting code and viewing results.
- **No Database Required**: Designed for simplicity, it stores no persistent application data.
- **Scalable**: Built with Django, making it easy to extend and integrate with other services.


## 🛠️ Technologies Used

### Backend:
- Python 3.x
- Django
- Scikit-learn (TF-IDF + LogisticRegression, RandomForestClassifier, MultinomialNB)
- Joblib (model persistence)
- NumPy

### Frontend:
- HTML5
- CSS3
- JavaScript (ES6+)

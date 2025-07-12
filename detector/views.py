from django.shortcuts import render
from django.http import JsonResponse
from joblib import load
import numpy as np
import os
import re

# Load the trained model
MODEL_PATH = 'detector/lang_detect_model.joblib'
LANGUAGE_DETECTOR_MODEL = None

try:
    LANGUAGE_DETECTOR_MODEL = load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    print(f"Model not found at {MODEL_PATH}. Please train and save the model.")

# Function to check if the input looks like programming code
def looks_like_code(code: str) -> bool:
    return bool(re.search(r'[;{}()\[\]=<>+\-*/]', code)) and len(code.split()) > 1

def home(request):
    result = None
    detected_languages = []
    error_message = None
    confidences = []

    if request.method == 'POST':
        code = request.POST.get('clean_code', '').strip()

        if LANGUAGE_DETECTOR_MODEL is not None and code:
            if not looks_like_code(code):
                result = "Invalid or Unknown Programming Language"
                detected_languages = ["Unknown"]
                confidences = ["<20%"]
            else:
                try:
                    # Get prediction probabilities
                    probabilities = LANGUAGE_DETECTOR_MODEL.predict_proba([code])[0]
                    class_labels = LANGUAGE_DETECTOR_MODEL.classes_

                    # Get top 3 indices sorted by confidence
                    top_indices = np.argsort(probabilities)[::-1][:3]
                    top_probs = probabilities[top_indices]
                    top_langs = class_labels[top_indices]

                    # Confidence thresholds
                    HIGH_CONFIDENCE_THRESHOLD = 0.50
                    MIN_VALID_CONFIDENCE = 0.20

                    # Case 1: High confidence → only one top language
                    if top_probs[0] >= HIGH_CONFIDENCE_THRESHOLD:
                        detected_languages = [top_langs[0]]
                        confidences = [f"{top_probs[0] * 100:.2f}%"]
                        result = f"Detected Language: {top_langs[0]}"

                    # Case 2: Top confidence is moderate → return top 3
                    elif top_probs[0] >= MIN_VALID_CONFIDENCE:
                        detected_languages = list(top_langs)
                        confidences = [f"{prob * 100:.2f}%" for prob in top_probs]
                        result = "Top Predictions:\n" + "\n".join(
                            [f"{i+1}. {detected_languages[i]}" for i in range(len(detected_languages))]
                        )

                    # Case 3: All too uncertain
                    else:
                        result = "Invalid or Unknown Programming Language"
                        detected_languages = ["Unknown"]
                        confidences = ["<20%"]

                    print(f"[DEBUG] Predictions: {list(zip(detected_languages, confidences))}")

                except Exception as e:
                    error_message = f"Error during prediction: {e}"
                    result = "Prediction Failed"
                    print(f"[ERROR] Prediction failure: {e}")

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'result': result,
                'top_languages': detected_languages,
                'top_confidences': confidences,
                'error_message': error_message
            }, status=200)

    return render(request, 'detector/index.html')

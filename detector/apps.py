from django.apps import AppConfig
import os
from joblib import load
from django.conf import settings

class DetectorAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detector'
    model_pipeline = None # Class variable to store the loaded model

    def ready(self):

        if not self.model_pipeline:
            model_path =load('detector/lang_detect_model.joblib')
            try:
                self.model_pipeline = model_path
                print(f"INFO: Language detection model loaded successfully from {model_path}")
            except FileNotFoundError:
                print(f"ERROR: Model file not found at {model_path}. Please check the path and file existence.")
            except Exception as e:
                print(f"ERROR: Failed to load model from {model_path}: {e}")
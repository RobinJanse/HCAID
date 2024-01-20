import html
import numpy as np
import pickle
import os
# Neccessary for the model
from django.conf import settings
from sklearn.preprocessing import LabelEncoder


class AIModelBad:
    def __init__(self):
        def load_model(filename):
            print("Loading model from file: ", filename)
            return pickle.load(open(filename, 'rb'))
        
        model_path = os.path.join(os.path.dirname(__file__), 'AI', 'models', 'mental_health_model.pkl')
        self.rfc_model = load_model(model_path)

    def predict_rfc(self, 
        employer_mental_health_benefits, 
        awareness_of_mental_health_coverage, 
        employer_discussed_mental_health, 
        employer_mental_health_resources, 
        anonymity_protection, 
        ease_of_medical_leave_for_mental_health,
        employer_react_negative_mental_health,
        employer_seriousness_mental_vs_physical,
        observed_consequences_mental_health,
        mental_health_impact_on_productivity
    ):
        print("Predicting using the bad model")
        
        X = np.array([[
            employer_mental_health_benefits, 
            awareness_of_mental_health_coverage, 
            employer_discussed_mental_health, 
            employer_mental_health_resources, 
            anonymity_protection, 
            ease_of_medical_leave_for_mental_health,
            employer_react_negative_mental_health,
            employer_seriousness_mental_vs_physical,
            observed_consequences_mental_health,
            mental_health_impact_on_productivity
        ]])
        prediction = self.rfc_model.predict(X)
        prediction_list = prediction.tolist()
        
        return prediction_list[0]
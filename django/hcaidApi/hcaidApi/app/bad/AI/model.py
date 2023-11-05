import html
import numpy as np
import pickle
import os
# Neccessary for the model
from django.conf import settings


class AIModelBad:
    def __init__(self):
        def load_model(filename):
            print("Loading model from file: ", filename)
            return pickle.load(open(filename, 'rb'))
        
        self.rfc_model = load_model(os.path.join(os.getcwd(), 'Model\\rfc_model.pkl'))

        # self.ann_model = load_model(os.path.join(settings.BASE_DIR, 'hcaidApi\\app\\bad\\AI\\models\\ann_model.pkl'))
        # self.svc_model = load_model(os.path.join(settings.BASE_DIR, 'hcaidApi\\app\\bad\\AI\\models\\svc_model.pkl'))

    def predict_bad(self, age, gender, country, seek_help, tech_company, remote_work):
        print("Predicting bad employee")
        print(age)

        X = np.array([0, 0, 0.4, 0, 0, 0]).reshape(1, -1)

        print("X: ", X)

        #X = self.scaler.transform(X)
        print("Using ANN model")
        prediction = self.ann_model.predict(X)
        print("Using SVC model: ", prediction)
        if(prediction == 1):
            prediction = self.svc_model.predict(X)
            print("Using SVC model: ", prediction)

        if(prediction < 0.5):
            prediction = 0
        else:
            prediction = 1
        return prediction
        
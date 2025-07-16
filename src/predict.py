# src/predict.py

from joblib import load
import numpy as np

model = load('model.pkl')  # Load trained model

def predict_popularity(features):
    features = np.array([features])
    return model.predict(features)[0]

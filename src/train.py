# src/train.py

import sys
import os
import numpy as np

# Add project root to sys.path to resolve imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preprocessing import load_and_preprocess
from src.model import get_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump

# Load and preprocess data
X, y = load_and_preprocess('D:\music_popularity_predictor\data\dataset.csv')

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Get model (default: Random Forest)
model = get_model("random_forest")

# Train model
model.fit(X_train, y_train)

# Save trained model to file
dump(model, 'model.pkl')

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("✅ Training complete")
print(f"📉 RMSE: {rmse:.2f}")
print(f"📈 R² Score: {r2:.2f}")

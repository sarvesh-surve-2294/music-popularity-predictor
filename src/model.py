# src/model.py

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def get_model(model_name="random_forest"):
    if model_name == "linear":
        return LinearRegression()
    elif model_name == "xgboost":
        return XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    elif model_name == "random_forest":
        return RandomForestRegressor(n_estimators=100, random_state=42)
    else:
        raise ValueError("Invalid model_name. Choose from: 'linear', 'random_forest', 'xgboost'")

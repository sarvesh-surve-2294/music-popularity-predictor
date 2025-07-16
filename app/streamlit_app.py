# app/streamlit_app.py

import sys
import os

# Add root directory to sys.path to resolve `src` module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_popularity
import streamlit as st

st.set_page_config(page_title="Spotify Popularity Predictor", page_icon="🎧")

st.title("🎧 Spotify Song Popularity Predictor")
st.markdown("Use audio features to predict the popularity score (0–100) of a track.")

# Sliders for numeric features
danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.slider("Energy", 0.0, 1.0, 0.5)
key = st.slider("Key (0=C, 1=C#/Db, ..., 11=B)", 0, 11, 5)
loudness = st.slider("Loudness (dB)", -60.0, 0.0, -10.0)
mode = st.selectbox("Mode", [0, 1], format_func=lambda x: "Minor" if x == 0 else "Major")
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.1)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.3)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)
liveness = st.slider("Liveness", 0.0, 1.0, 0.2)
valence = st.slider("Valence", 0.0, 1.0, 0.5)
tempo = st.slider("Tempo (BPM)", 40.0, 250.0, 120.0)
duration_ms = st.slider("Duration (ms)", 10000, 600000, 180000)
time_signature = st.selectbox("Time Signature", [3, 4, 5])

# On submit
if st.button("Predict Popularity"):
    features = [
        danceability, energy, key, loudness, mode, speechiness,
        acousticness, instrumentalness, liveness, valence,
        tempo, duration_ms, time_signature
    ]
    popularity = predict_popularity(features)
    st.success(f"🎯 Predicted Popularity Score: {round(popularity, 2)}")

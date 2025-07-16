# src/data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_and_preprocess(path='data/SpotifyTracks.csv'):
    df = pd.read_csv(path)

    # Drop unnecessary columns
    df = df.drop(columns=['Unnamed: 0', 'track_id', 'track_name', 'artists', 'album_name'])

    # Drop missing values
    df.dropna(inplace=True)

    # Select only the 13 features used in the Streamlit UI
    selected_features = [
        'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness', 'valence',
        'tempo', 'duration_ms', 'time_signature'
    ]

    # Define features and target
    features = df[selected_features]
    target = df['popularity']

    # Scale features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    return features_scaled, target

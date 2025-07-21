# 🎶 AlgoRhythm - Music Popularity Predictor

**AlgoRhythm** is an AI-powered machine learning application that predicts the popularity of a song based on its musical attributes. Built using Python, scikit-learn, and Streamlit, this project demonstrates how audio metadata can be used to forecast listener preferences and potential chart success.

---

## 🚀 Features

- 🎵 Predict song popularity using a trained Random Forest Regressor
- 📊 Preprocessed Spotify dataset with genre encoding and feature scaling
- ⚙️ Interactive web app built with Streamlit
- 🧠 Trained ML pipeline using scikit-learn
- 💾 Model persistence using `joblib` (`model.pkl`)


---

## 🎯 Input Features

- Acousticness  
- Danceability  
- Energy  
- Instrumentalness  
- Liveness  
- Loudness  
- Speechiness  
- Tempo  
- Valence  
- Duration (ms)  
- Key  
- Mode  
- Time Signature  
- Track Genre (encoded)

---

## 🛠️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/music-popularity-predictor.git
cd music-popularity-predictor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```
3. **Train the model**

```bash
python src/train.py
```

4. **Run the streamlit app**

```bash
streamlit run app/streamlit_app.py
```



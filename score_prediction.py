import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model


# Load model and preprocessing tools
model = load_model('ipl_score_predictor.h5')

venue_encoder = pickle.load(open('venue_encoder.pkl', 'rb'))
batting_team_encoder = pickle.load(open('batting_team_encoder.pkl', 'rb'))
bowling_team_encoder = pickle.load(open('bowling_team_encoder.pkl', 'rb'))
striker_encoder = pickle.load(open('striker_encoder.pkl', 'rb'))
bowler_encoder = pickle.load(open('bowler_encoder.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🏏 IPL Score Predictor")

# Input fields
venue = st.selectbox("Venue", venue_encoder.classes_)
bat_team = st.selectbox("Batting Team", batting_team_encoder.classes_)
bowl_team = st.selectbox("Bowling Team", bowling_team_encoder.classes_)
batsman = st.selectbox("Batsman", striker_encoder.classes_)
bowler = st.selectbox("Bowler", bowler_encoder.classes_)


# Predict button
if st.button("Predict Score"):
    # Encode input
    input_data = pd.DataFrame({
        'venue': [venue_encoder.transform([venue])[0]],
        'bat_team': [batting_team_encoder.transform([bat_team])[0]],
        'bowl_team': [bowling_team_encoder.transform([bowl_team])[0]],
        'batsman': [striker_encoder.transform([batsman])[0]],
        'bowler': [bowler_encoder.transform([bowler])[0]]
     })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0][0]
    st.success(f"🏆 Predicted Final Score: {round(prediction)} runs")

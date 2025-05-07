# IPL Score Prediction Using Deep Learning

## Project Overview

This project aims to predict the score of Indian Premier League (IPL) matches using Deep Learning techniques. By leveraging historical data of IPL matches, this model predicts the total score for an ongoing match based on various factors such as venue, batting team, bowling team, batsman, and bowler performance. The use of advanced deep learning algorithms ensures accurate predictions that could be valuable for analysts, commentators, and enthusiasts of the game.

## Streamlit Deployment Link : https://ipl-score-prediction-c5xqru3se3uujdmkqzv4v9.streamlit.app/


# Project Objective

The main objective of this project is to develop an AI-powered model that predicts IPL match scores using deep learning. This model can assist teams, analysts, and IPL enthusiasts in understanding the potential outcomes of matches based on current and historical data.

# Key Features

Score Prediction: The model predicts the total score of a match using input features such as the venue, batting team, bowling team, striker, and bowler.

Historical Data: It is trained on historical IPL match data from 2008 to 2017, considering performance metrics such as wickets, runs, overs, and more.

User-Friendly Interface: The model includes an interactive widget that allows users to input match parameters and get an immediate predicted score.

# Use Cases

For IPL Analysts: This tool can be used by analysts to forecast the performance of teams during a match and to gain insights into how various factors influence the score.

For Fantasy Cricket Players: Fantasy cricket players can use this tool to make informed decisions when selecting players for their fantasy teams by predicting likely match scores.

For IPL Fans: Fans can engage with the IPL in a new way by predicting scores and analyzing match dynamics based on historical trends.

For Commentators and Broadcasters: Commentators can utilize the model to create richer, more dynamic discussions on how match variables might affect final scores during live IPL broadcasts.

For Cricket Teams: Coaches and managers can use this model to assess the potential outcome of matches based on the opposition’s strengths and weaknesses.

# Tools and Technologies Used

Programming Language: Python

Machine Learning Framework: TensorFlow, Keras

Libraries: Pandas, NumPy, Matplotlib, Scikit-learn

Platform: Jupyter Notebook / Google Colab

Other Technologies: IPython Widgets for interactive visualization

# Dataset

The dataset contains historical IPL match data, including the following features:

Venue: The location of the match.

Batting Team: The team that is batting.

Bowling Team: The team that is bowling.

Striker and Bowler: The batsman and bowler in play.

Wickets, Runs, and Overs: Match statistics and performance indicators.

This data is used to train a deep learning model to predict the total score based on these variables.

# How the Model Works

Data Pre-processing: The historical IPL dataset is cleaned and pre-processed to handle missing values, remove irrelevant features, and encode categorical variables.

Model Architecture: The deep learning model is built using a neural network with multiple hidden layers and a linear output layer to predict continuous values (total score).

Training: The model is trained using historical match data, where features such as venue, batting team, and bowler are used to predict the match total score.

Prediction: Once trained, the model can predict scores for new match scenarios based on user input.


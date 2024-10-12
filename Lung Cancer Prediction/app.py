import numpy as np
import pandas as pd
import streamlit as st
import pickle




with st.form("lung_prediction"):
    # Heading of the page
    st.write("LUNG PREDICTION : ")
    
    # form inputs :
    # Required fields: ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY','PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING','ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH','SWALLOWING DIFFICULTY', 'CHEST PAIN', 'LUNG_CANCER']
    
    gender = 2 if st.radio("Gender : ", ("Male", "Female")) == "Male" else 1
    age = st.number_input("Age", min_value=1)    
    smoking = 2 if st.radio("Smoking", ("Yes", "No")) == "Yes" else 1
    yellow_fingers = 2 if st.radio("Yellow Fingers", ("Yes", "No")) == "Yes" else 1
    anxity = 2 if st.radio("Anxity", ("Yes", "No")) == "Yes" else 1
    peer_pressure = 2 if st.radio("Peer Pressure", ("Yes", "No")) == "Yes" else 1
    chronic_disease = 2 if st.radio("Chronic Disease", ("Yes", "No")) == "Yes" else 1
    fatigue = 2 if st.radio("Fatigue", ("Yes", "No")) == "Yes" else 1
    allergy = 2 if st.radio("Allergy", ("Yes", "No")) == "Yes" else 1
    wheezing = 2 if st.radio("Wheezing", ("Yes", "No")) == "Yes" else 1
    alcohol = 2 if st.radio("Alcohol", ("Yes", "No")) == "Yes" else 1
    coughing = 2 if st.radio("Coughing", ("Yes", "No")) == "Yes" else 1
    shortness_of_breath = 2 if st.radio("Shortness of Breath", ("Yes", "No")) == "Yes" else 1
    swallowing_difficulty = 2 if st.radio("Swallowing Difficulty", ("Yes", "No")) == "Yes" else 1
    chest_pain = 2 if st.radio("Chest Pain", ("Yes", "No")) == "Yes" else 1
    
    submit = st.form_submit_button("Predict")
    

if submit:
    with open("lung_cancer_prediction.pkl", "rb") as file:
        model = pickle.load(file)
        
    columns = ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY','PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING','ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH','SWALLOWING DIFFICULTY', 'CHEST PAIN']

    values = [gender, age, smoking, yellow_fingers, anxity, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]
    df = pd.DataFrame([values], columns=columns)
    
    # st.table(df)        
    
    prediction = model.predict(df)
    
    # st.write("prediction : ", prediction)
    
    if(prediction == "YES"):
        st.write("Sorry to inform you that You Have Lung Cancer")
        # st.write("You Have Lung Cancer")
    else:
        st.write("Happy News :))  You have No Lung Cancer")
        # st.write("You have No Lung Cancer")
    
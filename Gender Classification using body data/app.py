import streamlit as st 
import pandas as pd 
import numpy as np
import pickle
import os 

model_path = os.path.join(os.path.dirname(__file__), "gender_classification.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)
    
    
st.title("Gender Detection Using Facial Data ")


with st.form("gender_form"):
    
    fore_head_width = st.number_input("What is the width of your forehead (in cm)?", min_value=0.0, step=0.1)

    fore_head_height = st.number_input("What is the height of your forehead (in cm)?", min_value=0.0, step=0.1)

    long_hair = st.checkbox("Do you have long hair?")

    nose_wide = st.checkbox("Is your nose wide?")

    nose_long = st.checkbox("Is your nose long?")

    lips_thin = st.checkbox("Are your lips thin?")

    distance_nose_to_lip_long =st.checkbox("The Distance between Nose to Lips is Long or not")
    

    submit = st.form_submit_button(label="Predict (M/F)")
    



if submit:
    data = [long_hair, fore_head_width, fore_head_height, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
    
    prediction = model.predict([data])
    
    print(prediction)
    # st.write(prediction)
    gender = ""
    if prediction[0] : 
        gender = "Male"
    else:
        gender = "Female"
        # st.write("Female")
    st.markdown(
        f"""
        <div style="
            background-color: #0E1117; 
            padding: 15px; 
            border-radius: 10px; 
            # border: 2px solid #ddd; 
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            ">
            <h1 style="color: #333; text-align: center;">I Guss Your Gender Is </h1>
            <h2 style="color: #555; text-align: center;">{gender}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

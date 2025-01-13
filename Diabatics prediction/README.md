# Diabetes Prediction Web Application

This repository contains a Flask web application for predicting whether a person is diabetic or not based on input parameters. The model is trained using a dataset and is deployed with a user-friendly interface.\

# Features

- User-friendly web interface for diabetes prediction.

- Takes input parameters such as pregnancies, glucose levels, blood pressure, etc.

- Uses a pre-trained machine learning model (Diabetics_prediction.pkl) to make predictions.

- Returns prediction as Diabetic or No Diabetics.


# Input Parameters

The following parameters are used as input for predictions:

- Pregnancies: Number of times pregnant

- Glucose: Plasma glucose concentration

- BloodPressure: Diastolic blood pressure (mm Hg)

- SkinThickness: Triceps skinfold thickness (mm)

- Insulin: 2-Hour serum insulin (mu U/ml)

- BMI: Body Mass Index (weight in kg/(height in m)^2)

- DiabetesPedigreeFunction: Diabetes pedigree function

- Age: Age of the person


# Dependencies

- Flask

- Pandas

- Pickle

- scikit-learn

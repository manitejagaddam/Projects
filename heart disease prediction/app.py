


"""
['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol', 'FBS over 120',
       'EKG results', 'Max HR', 'Exercise angina', 'ST depression',
       'Slope of ST', 'Number of vessels fluro', 'Thallium']
"""


from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load the trained model
with open("heart_disease_prediction.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():
    # Extract form data
    age = request.form.get("age", type=int)
    sex = 1 if request.form.get("sex") == "male" else 0
    chest_pain = request.form.get("chest_pain", type=int)
    bp = request.form.get("bp", type=int)
    cholesterol = request.form.get("cholesterol", type=int)
    fbs = 1 if request.form.get("fbs") == "Yes" else 0
    ekg = request.form.get("ekg", type=int)
    max_hr = request.form.get("max_hr", type=int)
    exercise_angina = 1 if request.form.get("exercise_angina") == "Yes" else 0
    st_depression = request.form.get("st_depression", type=float)
    slope_st = request.form.get("slope_st", type=int)
    no_vesseles = request.form.get("no_vesseles", type=int)
    thallium = request.form.get("thallium", type=int)

    # Create DataFrame
    data = [[age, sex, chest_pain, bp, cholesterol, fbs, ekg, max_hr, exercise_angina, st_depression, slope_st, no_vesseles, thallium]]
    columns = ['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol', 'FBS over 120', 'EKG results', 'Max HR', 'Exercise angina', 'ST depression', 'Slope of ST', 'Number of vessels fluro', 'Thallium']
    df = pd.DataFrame(data, columns=columns)

    # Make prediction
    prediction = model.predict(df)
    
    # Return result to the user
    return f"Prediction: {'Heart disease' if prediction[0] == 1 else 'No heart disease'}"

if __name__ == "__main__":
    app.run(debug=True)

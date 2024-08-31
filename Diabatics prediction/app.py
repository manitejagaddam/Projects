from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load your model (replace 'model.pkl' with your actual model file)
model = pickle.load(open('Diabetics_prediction.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    Pregnancies = int(request.form.get("Pregnancies"))
    Glucose = int(request.form.get("Glucose"))
    BloodPressure = int(request.form.get("BloodPressure"))
    SkinThickness = int(request.form.get("SkinThickness"))
    Insulin = int(request.form.get("Insulin"))
    BMI = float(request.form.get("BMI"))
    DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
    Age = int(request.form.get("Age"))
    
    # Put data into a DataFrame
    input_data = pd.DataFrame({
        'Pregnancies': [Pregnancies],
        'Glucose': [Glucose],
        'BloodPressure': [BloodPressure],
        'SkinThickness': [SkinThickness],
        'Insulin': [Insulin],
        'BMI': [BMI],
        'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
        'Age': [Age]
    })

    # Predict using the loaded model
    prediction = model.predict(input_data)
    
    # The result will be the Outcome prediction
    outcome = int(prediction[0])  # Convert the prediction to a regular int
    outcomes = "No Diabetics" if outcome == 0 else "Diabetic"
    # Return the prediction as a JSON response
    return jsonify({'prediction': outcomes})
if __name__ == "__main__":
    app.run(debug=True, port=5001)

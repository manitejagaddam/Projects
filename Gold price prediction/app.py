"""
Needed inputs : 
    Date
    SPX
    GLD
    USO
    SLV
    
Output : 
    EUR/USD
"""
from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

# Load the pre-trained model
with open("GoldPricePrediction.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Retrieve form data
    date = request.form.get("date")
    spx = request.form.get("spx", type=float)
    gld = request.form.get("gld", type=float)
    uso = request.form.get("uso", type=float)
    slv = request.form.get("slv", type=float)

    # Prepare the data for prediction
    data = [[date, spx, gld, uso, slv]]
    columns = ['Date', 'SPX', 'GLD', 'USO', 'SLV']
    df = pd.DataFrame(data, columns=columns)
    
    # Data preprocessing
    def datePreprocessing(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df['Day'] = df['Date'].dt.day
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df.drop(columns=['Date'], inplace=True)
        return df
    
    df = datePreprocessing(df)
    
    # Predict using the model
    result = model.predict(df)
    
    # Format result as a string for response
    result_str = str(result[0])  # Assuming the model returns a single value

    # Return the prediction result
    
    return {"Prediction " : result_str}

if __name__ == "__main__":
    app.run(debug=True)

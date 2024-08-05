from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model pipeline
with open('loan_approval_pipeline.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

@app.route('/')
def home():

@app.route('/predict', methods=['POST'])    
def prediction():
    # no_of_dependents = request.form.get('no_of_dependents')
    # education = request.form.get('education')
    # self_employed = request.form.get('self_employed')
    # income_annum = request.form.get('income_annum')
    # loan_amount = request.form.get('loan_amount')
    # loan_term = request.form.get('loan_term')
    # cibil_score = request.form.get('cibil_score')
    # residential_assets_value = request.form.get('residential_assets_value')
    # commercial_assets_value = request.form.get('commercial_assets_value')
    # luxury_assets_value = request.form.get('luxury_assets_value')
    # bank_asset_value = request.form.get('bank_asset_value')
    # print(no_of_dependents)
    # print(bank_asset_value)
    data = request.get_json()
    
    
    df = pd.DataFrame([data])
    
    prediction = model_pipeline.predict(df)
    print(prediction)
    # print(data)
    # Return the result
    # return df
    return jsonify({'prediction': prediction[0]})
    # return no_of_dependents




if __name__ == '__main__':
    app.run(debug = True)
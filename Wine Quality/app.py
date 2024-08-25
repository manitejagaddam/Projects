"""
the required features are to built this app is :
1.Fixed acidity
2.Volatile acidity
3.Citric acid
4.Residual sugar
5.Chlorides
6.Free sulfur dioxide
7.Total sulfur dioxide
8.Density
9.pH
10.Sulphates
11.Alcohol

Output:
1.Quality

"""







from flask import Flask, render_template, redirect, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('Wine_Quality_Predicition.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict')
def predict():

    fixed_acidity = request.args.get('fixedAcidity', type=float)
    volatile_acidity = request.args.get('volatileAcidity', type=float)
    citric_acid = request.args.get('citricAcid', type=float)
    residual_sugar = request.args.get('residualSugar', type=float)
    chlorides = request.args.get('chlorides', type=float)
    free_sulfur_dioxide = request.args.get('freeSulfurDioxide', type=float)
    total_sulfur_dioxide = request.args.get('totalSulfurDioxide', type=float)
    density = request.args.get('density', type=float)
    ph = request.args.get('ph', type=float)
    sulphates = request.args.get('sulphates', type=float)
    alcohol = request.args.get('alcohol', type=float)
    list = []
    list.append(fixed_acidity)
    list.append(volatile_acidity)
    list.append(citric_acid)
    list.append(residual_sugar)
    list.append(chlorides)
    list.append(free_sulfur_dioxide)
    list.append(total_sulfur_dioxide)
    list.append(density)
    list.append(ph)
    list.append(sulphates)
    list.append(alcohol)
    list = [list]
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    
    df = pd.DataFrame(list, columns=columns)
    result = model.predict(df)
    # print(result)
    # ('Result : ', array([0], dtype=int64))
    ans = result[0]
    # print(ans)
    # print(type(ans))
    
    
    ans = {
        "YES" : "The Wine is good quality wine.",
        "NO" : "The Wine is not good quality wine"
    }
    
    
    if(ans == 0):
        print("Not")
    else:
        print('Yes')
    
    # return fixed_acidity
    return render_template("response.html", result = ans['NO'] if ans == 0 else ans["YES"])
    # try:
    #     # Get JSON data from the request
    #     data = request.get_json()

    #     # Example: print data to server log (you might process it or use a model here)
    #     print("Received data:", data)

    #     # Example response (replace with your prediction logic)
    #     response = {
    #         "message": "Prediction successful",
    #         "data_received": data
    #     }

    #     # Return the response as JSON
    #     return jsonify(response), 200

    # except Exception as e:
    #     # Handle errors
    #     print("Error:", e)
    #     return jsonify({"error": "An error occurred"}), 500











if __name__ == '__main__':
    app.run(debug=True)
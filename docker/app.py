# import libraries
from flask import Flask, request, jsonify
import joblib
import pandas as pd           
import numpy as np                     


# initialize the flask app
app = Flask(__name__) #automatically knows where this file lives

model = joblib.load('linear_reg.pkl')

# test route to confirm your API is live
@app.route('/')
def home():
    return "Model is Running"

# turn predict into an end point
# serach http methods

@app.route('/predict', methods = ['POST'])

def predict():
    
    data = request.get_json() # converst json into a python dictionary
    
    X = np.array(data['X']).reshape(1,-1)
    y_predict = float(model.predict(X))
    
    
    result = {
        
        'Penguin_Body_Mass': y_predict
    }
    
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
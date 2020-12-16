import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = np.array([float_features])
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    
    if output==1:
        return render_template('index.html', prediction_text='The customer will buy the term deposit!!!')

    else:
        return render_template('index.html', prediction_text='The customer will NOT buy the term deposit!!!')

if __name__ == "__main__":
    app.run(debug=True)
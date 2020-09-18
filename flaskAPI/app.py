'''
created on September 08, 2020
Author: swarali desai
'''
import flask
from flask import Flask, jsonify, request
import json
from data_input import dummy_data_in
import numpy as np
import pickle
import os


def load_models():
    file_name = "models/model_file.p"
    if os.path.exists(file_name):
        print(file_name)
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    # stub input features
    request_json = request.get_json()
    x = request_json['input']
    print(x)
    x_in = np.array(x).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

@app.route('/hello', methods=['GET'])
def hello():
    return "API is working",200


if __name__ == '__main__':
 application.run(debug=True)
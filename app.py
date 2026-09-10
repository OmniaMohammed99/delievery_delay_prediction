import pickle
from flask import Flask, request, jsonify,url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
# Load the trained model
model = pickle.load(open('delivery_delay_model.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb')) 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    # Convert data into a DataFrame
    input_data = pd.DataFrame(data)
    # Preprocess the input data
    input_data_preprocessed = preprocessor.transform(input_data)
    # Make predictions
    prediction = model.predict(input_data_preprocessed)
    # Convert prediction to a list and return as JSON
    return jsonify(prediction.tolist())

if __name__ == "__main__":
    app.run(debug=True)

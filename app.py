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

    # Make predictions
    prediction = model.predict(input_data)

    # Convert prediction to a list and return as JSON
    return jsonify(prediction.tolist())


@app.route('/predict', methods=['POST'])
def predict():

    data = request.form.to_dict()

    numeric_columns = [
        'item_count',
        'unique_products',
        'unique_sellers',
        'total_item_price',
        'total_freight',
        'total_order_value',
        'total_payment_value',
        'payment_count',
        'max_installments',
        'payment_type_count',
        'review_count',
        'avg_review_score',
        'order_purchase_year',
        'order_purchase_month',
        'order_purchase_day',
        'order_purchase_hour',
        'order_approved_at_year',
        'order_approved_at_month',
        'order_approved_at_day',
        'order_approved_at_hour'
    ]

    for column in numeric_columns:
        data[column] = float(data[column])

    # Keep categorical columns as strings
    data['customer_city'] = str(data['customer_city'])
    data['customer_state'] = str(data['customer_state'])

    # Create DataFrame
    input_data = pd.DataFrame([data])

    print("Input data:")
    print(input_data)


    # Make predictions
    prediction = model.predict(input_data)

    print("Prediction:", prediction)

    return render_template(
        'home.html',
        prediction_text=f'Predicted Delivery Delay: {prediction[0]}'
    )


if __name__ == "__main__":
    app.run(debug=True)

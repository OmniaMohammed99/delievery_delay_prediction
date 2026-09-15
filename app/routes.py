import pickle
from flask import Blueprint, request, jsonify, render_template, current_app 
import numpy as np
import pandas as pd


main = Blueprint("main", __name__)


def load_model():
    with open(current_app.config["MODEL_PATH"], "rb") as file:
        return pickle.load(file)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/predict_api", methods=["POST"])
def predict_api():
    model = load_model()

    data = request.json['data']
    print(data)
    # Convert data into a DataFrame
    input_data = pd.DataFrame(data)

    # Make predictions
    prediction = model.predict(input_data)

    # Convert prediction to a list and return as JSON
    return jsonify(prediction.tolist())


@main.route('/predict', methods=['POST'])
def predict():
    model = load_model()

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

    if prediction[0] == 1:
        result = "Delivery will be delayed"
    else:
        result = "Delivery will be on time"



    return render_template(
        'home.html',
        prediction_text= result
    )


if __name__ == "__main__":
    main.run(debug=True)

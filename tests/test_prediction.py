from pathlib import Path

import pandas as pd
import yaml

from src.prediction import load_model, predict


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = BASE_DIR / "config" / "config.yaml"


def load_config():

    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)


def create_sample_data():

    return pd.DataFrame({
        "customer_city": ["sao paulo"],
        "customer_state": ["SP"],
        "item_count": [1],
        "unique_products": [1],
        "unique_sellers": [1],
        "total_item_price": [50],
        "total_freight": [10],
        "total_order_value": [60],
        "payment_count": [1],
        "total_payment_value": [60],
        "max_installments": [1],
        "payment_type_count": [1],
        "review_count": [1],
        "avg_review_score": [5],
        "order_purchase_year": [2018],
        "order_purchase_month": [1],
        "order_purchase_day": [10],
        "order_purchase_hour": [10],
        "order_approved_at_year": [2018],
        "order_approved_at_month": [1],
        "order_approved_at_day": [10],
        "order_approved_at_hour": [10]
    })


def test_model_can_be_loaded():

    config = load_config()

    model_path = BASE_DIR / config["model_path"]

    model = load_model(model_path)

    assert model is not None


def test_model_can_predict():

    config = load_config()

    model_path = BASE_DIR / config["model_path"]

    model = load_model(model_path)

    input_data = create_sample_data()

    prediction = predict(model, input_data)

    assert len(prediction) == 1
    assert prediction[0] in [0, 1]
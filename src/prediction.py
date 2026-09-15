import pickle

model_path = 'models/delivery_delay_model.pkl'

def load_model(model_path):
    """
    Load the trained machine learning pipeline.
    """

    with open(model_path, "rb") as file:
        model = pickle.load(file)

    return model


def predict(model, input_data):
    """
    Make predictions using the trained model.
    """

    return model.predict(input_data)
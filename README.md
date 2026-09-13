# delievery_delay_prediction


A Flask web application that predicts whether an Olist order is likely to experience a delivery delay.

## Project Structure

```text
delievery_delay_prediction/
├── app/
├── config/
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
├── requirements/
├── run.py
└── README.md
```

## Requirements

* Python 3.11
* Flask==3.1.3
* pandas==3.0.5
* NumPy==2.4.6
* scikit-learn 1.7
* Flask


## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd delievery_delay_prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Install the runtime dependencies:

```bash
pip install -r requirements/requirements.txt
```

For development:

```bash
pip install -r requirements/requirements-dev.txt
```

## Model Files

Place the trained model files in:

```text
models/
├── delivery_delay_model.pkl
└── preprocessor.pkl
```

## Configuration

Application paths and parameters are stored in:

```text
config/config.yaml
```

Do not hardcode model paths or application parameters in the Python source code.

## Run the Application

Start the Flask application:

```bash
python run.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open the address in a web browser and enter the order information.

## Testing

Run the automated tests with:

```bash
pytest
```

## Model Output

The application returns:

* `0` — predicted no delivery delay
* `1` — predicted delivery delay

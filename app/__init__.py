from flask import Flask
from pathlib import Path
import yaml


def create_app():
    app = Flask(__name__)

    # Project root directory
    base_dir = Path(__file__).resolve().parent.parent

    # Load configuration
    config_path = base_dir / "config" / "config.yaml"

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    app.config["MODEL_PATH"] = base_dir / config["model_path"]
    app.config["HOST"] = config["host"]
    app.config["PORT"] = config["port"]
    app.config["DEBUG"] = config["debug"]

    # Import and register routes
    from app.routes import main

    app.register_blueprint(main)

    return app
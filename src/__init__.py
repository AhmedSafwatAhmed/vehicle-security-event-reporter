import json
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load config from JSON
    with open("config.json") as f:
        config = json.load(f)
        app.config.update(config)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

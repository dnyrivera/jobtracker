import os

from flask import Flask

from app.config import config_by_name


def create_app(config_name: str | None = None) -> Flask:
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "development")

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    from app.routes.main import main_bp

    app.register_blueprint(main_bp)

    return app

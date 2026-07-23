import logging
from flask import Flask
from config import Config

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s"
    )

    from app.routes.auth import auth_bp
    from app.routes.agenda import agenda_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(agenda_bp)

    return app
from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)  # still relative to module
    app.config.from_object(Config)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

from flask import Flask
from setting import DevConfig
from apps.users import user_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.register_blueprint(user_bp)

    return app
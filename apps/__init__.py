from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_map
from flask_jwt_extended import JWTManager


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'super-secret'
    db.init_app(app)
    jwt = JWTManager(app)
    from apps.students import app_students
    app.register_blueprint(app_students, url_prefix="/student")
    from apps.users import app_user
    app.register_blueprint(app_user, url_prefix="/user")
    return app

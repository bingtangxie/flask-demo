from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_map


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    from apps.students import app_students
    app.register_blueprint(app_students, url_prefix="/student")
    return app

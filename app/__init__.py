from os import remove

from flask import Flask
from .bcrypt import bcrypt
from .database import db
from app.api import api
from config import Config
from .routes import index

path = Config.SQLALCHEMY_DATABASE_URI
try:
    remove(path.replace('sqlite:///', ''))
except:
    pass

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api.init_app(app)
    bcrypt.init_app(app)
    app.register_blueprint(index)

    with app.app_context():
        db.create_all()

    return app

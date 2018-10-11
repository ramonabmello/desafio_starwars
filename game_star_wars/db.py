import flask_sqlalchemy
from .app import app

db = flask_sqlalchemy.SQLAlchemy(app)

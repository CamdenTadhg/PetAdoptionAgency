from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
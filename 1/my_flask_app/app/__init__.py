from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tusharsoni:admin123@localhost/tusharsoni'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)  # Generates a random secret key
    
    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)

    return app

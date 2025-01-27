from flask import Flask
from .routes import setup_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Set your secret key here
    return app
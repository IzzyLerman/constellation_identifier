from flask import Flask
import os
from .routes import setup_routes  # Import setup_routes from routes.py

def create_app():
    app = Flask(__name__)

    # Register routes
    setup_routes(app)

    return app

from flask import Flask
import os
from dotenv import load_dotenv
from app.routes import setup_routes

def create_app():
    app = Flask(__name__)
    setup_routes(app)  # Register routes
    return app

if __name__ == "__main__":
    load_dotenv()
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)

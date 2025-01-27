from flask import Blueprint, request, jsonify
from app.utils.prediction import make_prediction

bp = Blueprint('main', __name__)

@bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    prediction = make_prediction(data)
    #return jsonify({'prediction': prediction})

@bp.route('/')
def index():
    return jsonify({'message': "Hello, world!"})

def setup_routes(app):
    app.register_blueprint(bp)
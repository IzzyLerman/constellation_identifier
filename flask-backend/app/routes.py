from flask import Blueprint, request, jsonify
from app.utils.prediction import make_prediction
import os
from ultralytics import YOLO

bp = Blueprint('main', __name__)

@bp.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join('saved-imgs/', filename)
        file.save(file_path)
        #return jsonify({'prediction': prediction})
        model = YOLO('C:/constellation_identifier/runs/detect/trainyolo11m-1-17/weights/best.pt')
        results = model([file_path])
        classes = results[0].boxes.cls
        box_coords = results[0].boxes.xyxy
        response = []
        for i, cls in enumerate(classes):
            response.append({
                "Class": f"{cls}",
                "x1": int(box_coords[i][0]),
                "x2": int(box_coords[i][1]),
                "y1": int(box_coords[i][2]),
                "y2": int(box_coords[i][3])
            })
        return jsonify(response)


    else:
        return 'Invalid request method'
    
    
    

@bp.route('/')
def index():
    return jsonify({'message': "Hello, world!"})

def setup_routes(app):
    app.register_blueprint(bp)
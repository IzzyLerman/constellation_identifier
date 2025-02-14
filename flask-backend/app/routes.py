from flask import Blueprint, request, jsonify, Response
from app.utils.prediction import make_prediction
import os
from ultralytics import YOLO
from requests_toolbelt import MultipartEncoder
import json

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
        model = YOLO('C:/constellation_identifier/runs/detect/train15/weights/best.pt')
        results = model([file_path])
        results[0].save(f'processed-imgs/{filename}')
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
        json_response = json.dumps(response)
        m = MultipartEncoder(
           fields={'result_dict': json_response,
                    'result_img': (f'{filename}', open(f'processed-imgs/{filename}', 'rb'), 'text/plain')}
        )
        return Response(m.to_string(), mimetype=m.content_type)


    else:
        return 'Invalid request method'

@bp.route('/')
def index():
    return jsonify({'message': "Hello, world!"})

def setup_routes(app):
    app.register_blueprint(bp)
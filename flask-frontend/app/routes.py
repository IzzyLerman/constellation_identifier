from flask import render_template, request, jsonify, Blueprint
import os
import requests
from requests_toolbelt.multipart import decoder
import json

backend_port = 13520

bp = Blueprint('main', __name__)

def get_key(form_data):
    # 'form-data; name="birth_date"', 'content': b'2012-123'
    key = form_data.split(";")[1].split("=")[1].replace('"', '')

    print(key)

    return key

@bp.route('/')
def main_menu():
    return render_template('main.html')

@bp.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'

    filename = file.filename
    file_path = os.path.join('static/saved-imgs/', filename)
    file.save(file_path)

    url = f'http://localhost:{backend_port}/predict'
    files = {'file': open(file_path, 'rb')}

    r=requests.post(url, files=files)
    multipart_data = decoder.MultipartDecoder.from_response(r)
    json_response = None
    image_bytes = None

    for part in multipart_data.parts:
        cd = part.headers.get(b'Content-Disposition', b'').decode()
        if 'result_dict' in cd:
            json_response = json.loads(part.text)
        elif 'result_img' in cd:
            image_bytes = part.content  # binary image data

    with open('static/processed-imgs/output_image.png', 'wb') as file:
        file.write(image_bytes)

    return render_template('upload.html', pred=json_response, filename="output_image.png")

def setup_routes(app):
    app.register_blueprint(bp)
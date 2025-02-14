from flask import Flask, render_template, request, jsonify, url_for
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def setup_routes(app):
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    @app.route("/")
    def index():
        return render_template("upload.html")  # Loads the upload page

    @app.route("/upload", methods=["POST"])
    def upload_file():
        if "image" not in request.files:
            return jsonify({"success": False, "error": "No file part"})

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"success": False, "error": "No selected file"})

        # Ensure valid file extension
        if file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            return jsonify({
                "success": True,
                "image_url": url_for('static', filename=f'uploads/{file.filename}')
            })

        return jsonify({"success": False, "error": "Invalid file type"})


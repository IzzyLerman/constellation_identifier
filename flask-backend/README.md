# Flask Backend Project

This project is a Flask application that handles predictions using a pretrained machine learning model. It exposes a POST endpoint at `/predict` for making predictions based on input data.

## Project Structure

```
flask-backend
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── model
│   │   └── pretrained_model.pkl
│   └── utils
│       └── prediction.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app/main.py
   ```

2. Make a POST request to the `/predict` endpoint with the required input data. Example using `curl`:
   ```
   curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"input_data": [your_data_here]}'
   ```

## License

This project is licensed under the MIT License.
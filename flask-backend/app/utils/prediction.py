def make_prediction(input_data):
    import pickle
    import numpy as np

    # Load the pretrained model
    with open('app/model/pretrained_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Process the input data (assuming it's a list of features)
    processed_data = np.array(input_data).reshape(1, -1)

    # Make a prediction
    prediction = model.predict(processed_data)

    return prediction.tolist()
from ultralytics import YOLO
from ray import tune

model = YOLO('yolo11m.pt')

def train_model():

    results = model.train(data='datasets/data.yaml', epochs=25)

    metrics = model.val()  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75'''
    '''
    search_space = {
        "hsv_h" : (0.0, 0.1),
        "hsv_s" : (0.0, 0.9),
        "hsv_v" : (0.0, 0.9),
    }
    
    model.tune(
        data="datasets/data.yaml",
        epochs=30,
        iterations=300,
        optimizer="AdamW",
        space=search_space,
        plots=True,
        save=True,
        val=True,
    )
    '''

if __name__ == '__main__':
    train_model()
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def train_model():

    results = model.train(data='datasets/data.yaml', epochs=20)

    metrics = model.val()  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75

if __name__ == '__main__':
    train_model()
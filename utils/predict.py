from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('C:/constellation_identifier/runs/detect/trainyolo11m-1-17/weights/best.pt')
    results = model([
                    'C:/constellation_identifier/datasets/test/images/2022-01-05-00-00-00-s_png_jpg.rf.098ebe8a5c09f983736111049dfefc1d.jpg',
                    'C:/constellation_identifier/datasets/test/images/2022-01-06-00-00-00-n_png_jpg.rf.fa81432a47e707b9a9e242896afc9529.jpg'
                    ])
    
    
    for i,r in enumerate(results):
        print(f"Image {i+1}")
        #print(r.boxes)
        #print(r.boxes.cls)
        r.show()
    

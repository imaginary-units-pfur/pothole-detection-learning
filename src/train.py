from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s.pt')  # load a pretrained model (recommended for training)

model.train(
    data='cfg.yaml',
    batch=64,
    imgsz=640,
    pretrained=True,
    verbose=True,
    half=True,
    patience=30,
    cache=False, 
    mixup=0.5, 
    mosaic=0.3, 
    flipud=0.3, 
    degrees=0.3,
)

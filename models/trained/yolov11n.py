import os
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

DATA_YAML = os.path.join(os.path.dirname(__file__), "../../datasets/data.yaml")

results = model.train(data=DATA_YAML, epochs=20, imgsz=640, batch=16, name="yolo11n_football")
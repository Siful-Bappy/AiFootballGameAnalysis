from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict("video_test/dataset.mp4", save=True)
print(results[0])
for box in results[0].boxes:
    print(box)
    x1, y1, x2, y2 = box.xyxy[0]
    # print(f"Detected box: {x1}, {y1}, {x2}, {y2}")

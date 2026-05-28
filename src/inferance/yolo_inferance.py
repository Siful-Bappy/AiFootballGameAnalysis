import os
import cv2
from ultralytics import YOLO

MODEL_PATH  = os.path.join(os.path.dirname(__file__), "../../models/weights/best.pt")
INPUT_VIDEO = os.path.join(os.path.dirname(__file__), "../../video_test/dataset.mp4")
OUTPUT_VIDEO = os.path.join(os.path.dirname(__file__), "../../video_test/output.avi")

model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(INPUT_VIDEO)
assert cap.isOpened(), f"Cannot open video: {INPUT_VIDEO}"

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(OUTPUT_VIDEO, cv2.VideoWriter_fourcc(*"XVID"), fps, (width, height))

frame_num = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(frame, conf=0.3)[0]
    annotated = result.plot()

    out.write(annotated)

    cv2.imshow("Football Detection", annotated)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # press Q to quit early
        break

    frame_num += 1
    print(f"Frame {frame_num}", end="\r")

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"\nSaved to {OUTPUT_VIDEO}")

from ultralytics import YOLO
import cv2

INPUT_VIDEO = "dataset.mp4"
OUTPUT_VIDEO = "output.mp4"
MODEL = "yolo11n.pt"


def main():
    model = YOLO(MODEL)

    cap = cv2.VideoCapture(INPUT_VIDEO)
    assert cap.isOpened(), f"Cannot open video: {INPUT_VIDEO}"

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(
        OUTPUT_VIDEO,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )

    frame_num = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        annotated = results.plot()

        out.write(annotated)
        frame_num += 1
        print(f"Frame {frame_num}", end="\r")

    cap.release()
    out.release()
    print(f"\nDone. Saved to {OUTPUT_VIDEO}")


if __name__ == "__main__":
    main()

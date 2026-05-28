import cv2 as cv

read_video = cv.VideoCapture("dataset.mp4")
if not read_video.isOpened():
    raise ValueError("Cannot open video: dataset.mp4")

frames = []
while True:
    ret, frame = read_video.read()
    if not ret:
        break

    print(frame.shape)
    print(frame)
    print("----")

    frames.append(frame)
    print(f"Read {len(frames)} frames", end="\r")
    print("Frames: ", frames)
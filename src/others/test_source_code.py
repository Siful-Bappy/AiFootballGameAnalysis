import os
import cv2 as cv

VIDEO_PATH = os.path.join(os.path.dirname(__file__), "../../video_test/dataset.mp4")
read_video = cv.VideoCapture(VIDEO_PATH)
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
    # print(f"Read {len(frames)} frames", end="\r")
    # print("Frames: ", frames)
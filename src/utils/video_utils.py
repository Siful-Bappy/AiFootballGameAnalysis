import cv2 as cv

def read_video(video_path):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")
    
    frames = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(frames, output_path, fps=24):
    if not frames:
        raise ValueError("No frames to save.")
    
    height, width, _ = frames[0].shape
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(output_path, fourcc, fps, (width, height))
    
    for frame in frames:
        out.write(frame)
    
    out.release()
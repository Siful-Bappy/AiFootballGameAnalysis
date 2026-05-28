from src.utils import read_video, save_video

def main():
    frames = read_video("video_test/dataset.mp4")
    save_video(frames, "video_test/output.avi")

if __name__ == "__main__":
    main()
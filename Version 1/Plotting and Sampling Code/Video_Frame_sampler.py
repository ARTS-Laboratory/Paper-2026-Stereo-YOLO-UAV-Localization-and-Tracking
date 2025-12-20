import cv2
import os
import numpy as np

def extract_uniform_frames_opencv(video_path, output_folder, num_frames=11):
    # Open video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    # Get total frames and FPS
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps

    print(f"Video FPS: {fps}, Total Frames: {total_frames}, Duration: {duration:.2f}s")

    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Calculate target frame indices
    frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)

    for i, frame_idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            frame_filename = os.path.join(output_folder, f"R{i+1:02d}.png")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")
        else:
            print(f"Warning: Could not read frame at index {frame_idx}")

    cap.release()

# Example usage
extract_uniform_frames_opencv("Drone Flight R.mp4", "output_frames")

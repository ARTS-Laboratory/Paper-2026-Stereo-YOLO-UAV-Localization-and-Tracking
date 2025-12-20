import cv2
import os
import numpy as np
import pandas as pd
import subprocess

# Define frame sampling function
def extract_uniform_frames_opencv(video_path, output_folder, num_frames):
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
    frame_indices = np.linspace(0, total_frames, num_frames, dtype=int)
    frame_numbers = [(indices-1) for indices in frame_indices]

    for i, frame_idx in enumerate(frame_numbers):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            frame_filename = os.path.join(output_folder, f"F{i+0:03d}.png")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")
        else:
            print(f"Warning: Could not read frame at index {frame_idx}")

    cap.release()

# Sample frames from right camera video
extract_uniform_frames_opencv("Jul_2_FLIR_Right_Flight_1.mp4", "Jul_2_FLIR_Right_Flight_1_Sampled_Frames", 276)

# Sample frames from left camera video
extract_uniform_frames_opencv("Jul_2_FLIR_Left_Flight_1.mp4", "Jul_2_FLIR_Left_Flight_1_Sampled_Frames", 276)

# Define variables for right camera
marked_output_folder = "Jul_2_FLIR_Right_Flight_1_Hand_Marked_Sampled_Frames"
excel_file = "Jul_2_FLIR_Right_Flight_1_Hand_Marked_Sampled_Frames.xlsx"
image_folder = "Jul_2_FLIR_Right_Flight_1_Sampled_Frames"
horizontal_axis = 'Z'
vertical_axis = 'Y'
horizontal_adjust = '0'

subprocess.run(['python','Frame_marker_code.py',marked_output_folder, excel_file, image_folder, horizontal_axis, vertical_axis, horizontal_adjust])

# Define variables for left camera
marked_output_folder = "Jul_2_FLIR_Left_Flight_1_Hand_Marked_Sampled_Frames"
excel_file = "Jul_2_FLIR_Left_Flight_1_Hand_Marked_Sampled_Frames.xlsx"
image_folder = "Jul_2_FLIR_Left_Flight_1_Sampled_Frames"
horizontal_axis = 'X'
vertical_axis = 'Y'
horizontal_adjust = '3840'

subprocess.run(['python','Frame_marker_code.py',marked_output_folder, excel_file, image_folder, horizontal_axis, vertical_axis, horizontal_adjust])

# frame_indices = np.linspace(0, 10, 6, dtype=int)
# print(frame_indices)
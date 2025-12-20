import os
import cv2
import sys
import pandas as pd
import numpy as np
import re

# marked_output_folder = "Jul_2_FLIR_Right_Flight_1_Hand_Marked_Sampled_Frames"
# excel_file = "Jul_2_FLIR_Right_Flight_1_Hand_Marked_Sampled_Frames.xlsx"
# image_folder = "Jul_2_FLIR_Right_Flight_1_Sampled_Frames"
# horizontal_axis = 'Z'
# vertical_axis = 'Y'
# horizontal_adjust = '0'

marked_output_folder = "Jul_2_FLIR_Left_Flight_1_Hand_Marked_Sampled_Frames"
excel_file = "Jul_2_FLIR_Left_Flight_1_Hand_Marked_Sampled_Frames.xlsx"
image_folder = "Jul_2_FLIR_Left_Flight_1_Sampled_Frames"
horizontal_axis = 'X'
vertical_axis = 'Y'
horizontal_adjust = '3840'

# Retrieve variables from Hand_labeled_drone_tracking.py
# marked_output_folder = sys.argv[1]
# excel_file = sys.argv[2]
# image_folder = sys.argv[3]
# horizontal_axis = sys.argv[4]
# vertical_axis = sys.argv[5]
# horizontal_adjust = sys.argv[6]

# Define the append process to add coordinates to the Excel sheet
def append_df1_to_excel(df1, excel_path):
    df1_excel = pd.read_excel(excel_path)
    result = pd.concat([df1_excel, df1], ignore_index=True)
    result.to_excel(excel_path, index=False)

# Define files sorting by number in file name
def numerical_sort(value):
    numbers = re.compile(r'\d+')
    parts = numbers.split(value)
    parts[1:2] = map(int, numbers.findall(value))
    return parts

# Create a folder to save the images with the marked points if it doesn't exist
if not os.path.exists(marked_output_folder):
    os.makedirs(marked_output_folder)

# Global variable to store the clicked point coordinates
clicked_point = None

# Function to be called when a point is clicked
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse click
        global clicked_point
        clicked_point = (x, y)
        # Mark the clicked point with a red cross
        cv2.drawMarker(image, (x, y), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=40, thickness=6)
        
        # Print the X, Y coordinates on the image
        cv2.putText(image, f'({int(horizontal_adjust)-x},{2160-y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)

        # Show the image with the marked point
        cv2.imshow("Image", image)

        df1=pd.DataFrame([["{}".format(int(horizontal_adjust)-x),'{}'.format(2160-y)]],columns=[horizontal_axis, vertical_axis])
        print(df1)
        # df1.to_excel('Trimmed_Drone_Flight_L.xlsx')
        append_df1_to_excel(df1, excel_file)

# List all PNG images in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

# Loop through each image file after sorting
for image_name in sorted(image_files, key=numerical_sort):
    # Read the image
    image_path = os.path.join(image_folder, image_name)
    image = cv2.imread(image_path)
    
    # Show the image and set up the mouse callback for clicking
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", on_click)

    # Wait until the user clicks on the image
    while clicked_point is None:
        cv2.waitKey(1)  # Wait for a key event or mouse click

    # Save the image with the marked point
    output_path = os.path.join(marked_output_folder, image_name)
    cv2.imwrite(output_path, image)

    # Reset clicked point for the next image
    clicked_point = None

    # Close the image window after processing
    cv2.destroyAllWindows()
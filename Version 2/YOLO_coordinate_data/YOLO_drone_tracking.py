from ultralytics import YOLO
import multiprocessing
import pandas as pd
import openpyxl

# Define the append process to add coordinates to the Excel sheet for left camera
def append_df1_to_excel(df1, excel_path):
    df1_excel = pd.read_excel(excel_path)
    result = pd.concat([df1_excel, df1], ignore_index=True)
    result.to_excel(excel_path, index=False)
# Define the append process to add coordinates to the Excel sheet for right camera
def append_df2_to_excel(df2, excel_path):
    df2_excel = pd.read_excel(excel_path)
    result = pd.concat([df2_excel, df2], ignore_index=True)
    result.to_excel(excel_path, index=False)

# Create a new YOLO model from scratch
# model = YOLO("yolo11n.yaml")

# Load a pretrained YOLO model (recommended for training)
model = YOLO("Drone_Only_Training_v2.pt")

# Train the model using the 'coco8.yaml' dataset for 50 epochs
# results = model.train(data="data.yaml", epochs=50)

# Evaluate the model's performance on the validation set
# results = model.val()

# Perform object detection on an image using the model

# Take results from left camera and process through YOLO. Then flip each coordinate to our desired axes direction (X and Y).
def camL():
    results = model(source="Edited_FLIR_Left_Flight_1.mp4",save=True,vid_stride=1,conf=0.50,iou=0.1,stream=True)
    for result in results:
        boxes = result.boxes.xywh
        for box in boxes:
            x, y, w, h = box
            df1=pd.DataFrame([["{}".format(3840-x),'{}'.format(2160-y)]],columns=['X','Y'])
            print(df1)
            # df1.to_excel('Trimmed_Drone_Flight_L.xlsx')
            append_df1_to_excel(df1,'Edited_FLIR_Left_Flight_1.xlsx')

# Take results from right camera and process through YOLO. Then flip each coordinate to our desired axes direction (Z and Y).
def camR():
    results = model(source="Edited_FLIR_Right_Flight_1.mp4",save=True,vid_stride=1,conf=0.50,iou=0.1,stream=True)
    for result in results:
        boxes = result.boxes.xywh
        for box in boxes:
            x, y, w, h = box
            # print("Z-position: {}, Y-position: {}".format(x, 2160-y))
            df2=pd.DataFrame([["{}".format(x),'{}'.format(2160-y)]],columns=['Z','Y'])
            print(df2)
            # df2.to_excel('Trimmed_Drone_Flight_R.xlsx')
            append_df2_to_excel(df2,'Edited_FLIR_Right_Flight_1.xlsx')



### START DATA SAMPLING PROCESS ###

def dataSampling():
    # Load your Excel file for LEFT camera
    df = pd.read_excel("Trimmed_Drone_Flight_L.xlsx", skiprows=[1])  # Replace with your actual file name

    # Uniformly select 10 rows from the DataFrame
    selected_rows = df.iloc[::len(df)//10][:10]  # This samples evenly spaced rows

    # Save the selected rows to a new Excel file
    selected_rows.to_excel("Sampled_Trimmed_Drone_Flight_L.xlsx", index=False)


    # Load your Excel file for RIGHT camera
    df = pd.read_excel("Trimmed_Drone_Flight_R.xlsx",skiprows=[1])  # Replace with your actual file name

    # Uniformly select 10 rows from the DataFrame
    selected_rows = df.iloc[::len(df)//10][:10]  # This samples evenly spaced rows

    # Save the selected rows to a new Excel file
    selected_rows.to_excel("Sampled_Trimmed_Drone_Flight_R.xlsx", index=False)

    print("Created new Excel files for sampled coordinates")

### END DATA SAMPLING PROCESS ###



if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=camL)
    p2 = multiprocessing.Process(target=camR)
    p3 = multiprocessing.Process(target=dataSampling)

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    p3.start()



# detection
    # with open("trimmed_flight_output_YOLO_coordinates/L10.txt", "a") as f:
        # print(result.boxes.xyxy, file=f)   # box with xyxy format, (N, 4)
        # print(result.boxes.xywh, file=f)   # box with xywh format, (N, 4)
        # print(result.boxes.xyxyn, file=f)  # box with xyxy format but normalized, (N, 4)
        # print(result.boxes.xywhn)  # box with xywh format but normalized, (N, 4)
        # print(result.boxes.conf, file=f)   # confidence score, (N, 1)
        # print(result.boxes.cls, file=f)   # cls, (N, 1)

    # # segmentation
    # print(result.masks.masks)     # masks, (N, H, W)
    # print(result.masks.segments)  # bounding coordinates of masks, List[segment] * N

    # # classification
    # print(result.probs)     # cls prob, (num_class, )
    
# Export the model to ONNX format
# success = model.export(format="onnx")

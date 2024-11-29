import cv2
import cvzone
import math
import numpy as np
import tempfile
import streamlit as st
from sort import *
from ultralytics import YOLO




classNames = [ "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]




# Streamlit Title
st.title("Vehicle Counter App")

# Video Upload
uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])




if uploaded_video is not None:
    
    
    # Save the uploaded video to a temporary file
    temp_video_file = tempfile.NamedTemporaryFile(delete=False)
    temp_video_file.write(uploaded_video.read())
    temp_video_file_path = temp_video_file.name

    # Load YOLO model
    model = YOLO("yoloWeights/yolov8n.pt")

    # Initialize SORT tracker
    tracker = Sort(max_age=100, min_hits=5, iou_threshold=0.4)

    # Line limits for vehicle counting
    limits = [400, 297, 673, 297]
    car_counts = []
    
    
    vehicle_options = ["all", "car", "bicycle", "truck", "bus", "motorbike", "fire hydrant"]

    # Multiselect for selecting multiple vehicle types
    selected_vehicles = st.multiselect("Select the vehicle types to count:", vehicle_options, default=None)
    
    print(selected_vehicles)
    print(type(selected_vehicles))

    if st.button("Submit"):
        
        if selected_vehicles:
        
            cap = cv2.VideoCapture(temp_video_file_path)
            stframe = st.empty()  # Placeholder for video frames
            
            

            while cap.isOpened():
                success, img = cap.read()
                if not success:
                    break
                # YOLO object detection
                result = model(img, stream=True)
                detections = np.empty((0, 5))

                for r in result:
                    boxes = r.boxes
                    for box in boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        conf = math.ceil(box.conf[0] * 100) / 100
                        cls = int(box.cls[0])
                        currentClass = model.names[cls]

                        if currentClass in selected_vehicles and conf > 0.3:
                            w, h = x2 - x1, y2 - y1
                            cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(0, 0, 255))
                            currentArray = np.array([x1, y1, x2, y2, conf])
                            detections = np.vstack((detections, currentArray))

                # Update SORT tracker
                resultTracker = tracker.update(detections)


                for result in resultTracker:
                    x1, y1, x2, y2, id = map(int, result)

                    
                    if id not in car_counts:
                        car_counts.append(id)

                # Display count
                cv2.putText(img, f"Count: {len(car_counts)}", (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

                # Render frame in Streamlit
                stframe.image(img, channels="BGR", use_container_width=True)

            cap.release()
            
            # st.write("Total cars count is ", len(car_counts))
            st.markdown(f"<h1 style='text-align: center; color: white;'>Total Cars Count: {len(car_counts)}</h1>", unsafe_allow_html=True)

        else:
            st.write("No vehicle types selected.")

    # Open video
    
import cv2
import cvzone
import math
import numpy as np
import tempfile
import streamlit as st
from sort import *
from ultralytics import YOLO

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

    # Load mask (optional, replace with your mask file or remove this block)
    try:
        mask = cv2.imread("mask.png")
    except:
        mask = None

    # Initialize SORT tracker
    tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.2)

    # Line limits for vehicle counting
    limits = [400, 297, 673, 297]
    car_counts = []

    # Open video
    cap = cv2.VideoCapture(temp_video_file_path)
    stframe = st.empty()  # Placeholder for video frames

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        # Apply mask if available
        if mask is not None:
            imgRegion = cv2.bitwise_and(img, mask)
        else:
            imgRegion = img

        # YOLO object detection
        result = model(imgRegion, stream=True)
        detections = np.empty((0, 5))

        for r in result:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = math.ceil(box.conf[0] * 100) / 100
                cls = int(box.cls[0])
                currentClass = model.names[cls]

                if currentClass in ['car', 'truck', 'bus', 'motorbike'] and conf > 0.3:
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

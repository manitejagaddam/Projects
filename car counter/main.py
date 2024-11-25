import cv2
import cvzone
import math

from ultralytics import YOLO


model = YOLO('yoloWeights\yolov8n.pt')

cap = cv2.VideoCapture("cars.mp4")


classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush" ]



mask = cv2.imread('mask.png')


while True:

    sucess, img = cap.read()

    # imgRegion = cv2.bitwise_and(img, mask)

    result = model(img, stream= True)


    for r in result:

        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]

            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w = x2 - x1
            h = y2 - y1

            cvzone.cornerRect(img, bbox = (x1, y1, w, h), l = 1)

            conf = (math.ceil(box.conf[0] * 100)) / 100

            cls = int(box.cls[0])

            cvzone.putTextRect(img, text = f'{classNames[cls]} {conf}', pos=(max(5, x1), max(30, y1)), scale = 1, thickness= 1, colorR=(0,0,0) )



    cv2.imshow("Car_Counter", img)
    # cv2.imshow("Car Counter", imgRegion)
    cv2.waitKey(1)

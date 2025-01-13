import cv2
import cvzone
import math

from sort import *

from ultralytics import YOLO


model = YOLO("yoloWeights\yolov8n.pt")

cap = cv2.VideoCapture("cars.mp4")


classNames = [ "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush",
]


mask = cv2.imread("mask.png")
print(mask.shape)


tracker = Sort(max_age = 20, min_hits = 3, iou_threshold=0.2)

limits = [400, 297, 673, 297]


car_counts = []


while True:
    sucess, img = cap.read()

    imgRegion = cv2.bitwise_and(img, mask)

    result = model(imgRegion, stream= True)
    # result = model(img, stream=True)

    # print(img.shape)
    
    
    detections = np.empty((0,5  ))
    

    for r in result:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]

            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w = x2 - x1
            h = y2 - y1

            cvzone.cornerRect(imgRegion, bbox=(x1, y1, w, h), l=1)

            conf = (math.ceil(box.conf[0] * 100)) / 100

            cls = int(box.cls[0])
            
            currentClass = classNames[cls]
            
            if currentClass == 'car' or currentClass == 'truck' or currentClass == 'bus' or currentClass == 'motorbike'  and conf > 0.3:

                # cvzone.putTextRect( imgRegion, text=f"{classNames[cls]} {conf}", pos=(max(5, x1), max(30, y1)), scale=1, thickness=1, colorR=(0, 0, 0) )
                cvzone.cornerRect(img, (x1, y1, w, h), l = 9, rt = 2, colorR = (0,0,0))
                
                
                currentArray = np.array([x1, y1, x2, y2, conf])
                
                detections = np.vstack((detections, currentArray))
                
    resultTracker = tracker.update(detections)

    # cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 250), 5)
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 250), 5)

    for result in resultTracker:

        x1, y1, x2, y2, id = result
        
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        print(result)
        
        w, h = x2 - x1, y2 - y1
        
        # cvzone.cornerRect(img, (x1, y1, w, h), l = 9, rt = 2, colorR = (0,0,0))
        
        # cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), (max(30, y1))), scale = 1, thickness = 1)
        
        cx, cy = x1 + w // 2, y1 + h // 2
        
        if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[1] + 15:
            if car_counts.count(id) == 0:
                car_counts.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

        # cvzone.putTextRect(img, f' Count: {str(len(car_counts))}', (50, 50))
        cv2.putText(img,f"{str(len(car_counts))}",(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,100,255),7)


            




    cv2.imshow("Car_Counter", img)
    # cv2.imshow("Car Counter", imgRegion)
    cv2.waitKey(1)

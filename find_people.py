import torch
import cv2
from ultralytics import YOLO

model = YOLO('yolov9c.pt')  

video_capture = cv2.VideoCapture(0) 

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    results = model(frame)

    detections = results.pred[0]

    people = detections[detections[:, 5] == 0]

    for detection in people:
        x1, y1, x2, y2, confidence, class_id = detection.tolist()[:6]
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(frame, f'Person {confidence:.2f}', (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
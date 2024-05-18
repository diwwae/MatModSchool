import cv2
import os
import pandas as pd
from ultralytics import YOLO

video_path = 'video.mp4'
output_folder = 'frames'

os.makedirs(output_folder, exist_ok=True)
cap = cv2.VideoCapture(video_path)
print(cap)
count = 0
success = True
    
while success:
    success, frame = cap.read()
    if success:
        frame_path = os.path.join(output_folder, f"frame_{count:05d}.jpg")
        cv2.imwrite(frame_path, frame)
        count += 1

cap.release()
print(f"Видео разбито на {count} кадров")

frames = sorted(os.listdir(output_folder))
data = {'frame': frames}
df = pd.DataFrame(data) 

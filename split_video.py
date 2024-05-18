import cv2
import os
import pandas as pd

# Функция для разбиения видео на кадры
def video_to_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
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

# Функция для создания таблицы данных
def create_frame_table(output_folder):
    frames = sorted(os.listdir(output_folder))
    data = {'frame': frames}
    df = pd.DataFrame(data)
    return df

video_path = 'video.mp4'
output_folder = 'frames'
video_to_frames(video_path, output_folder)
df = create_frame_table(output_folder)

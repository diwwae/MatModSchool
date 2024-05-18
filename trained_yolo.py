from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')

result = model(source = 'video.mp4',show = True, conf = 0.3, save = True)
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2


m1 = YOLO("yolov8s.pt")
results = m1.predict(source="0", show = True)
print(results)
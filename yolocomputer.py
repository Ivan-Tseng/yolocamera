
from ultralytics import YOLO

# Load an official or custom model
model = YOLO('yolov8n.pt')  # 仔入自己的權重位置
# model = YOLO('yolov8n-seg.pt')  # Load an official Segment model
# model = YOLO('yolov8n-pose.pt')  # Load an official Pose model
# model = YOLO('path/to/best.pt')  # Load a custom trained model

# Perform tracking with the model
# results = model.track(source="screen", show=True)  # 辨識電腦螢幕的追蹤
results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)  #網頁追蹤

# results = model.track(source="auto", show=True)  # 攝影機

# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # Tracking with ByteTrack tracker
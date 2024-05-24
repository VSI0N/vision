from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import torch
import numpy as np

app = Flask(__name__)

# Load the YOLO model and ensure it uses the GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = YOLO("yolov8s.pt").to(device)

# Set webcam resolution
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

ZONE_POLYGON = np.array([[0, 0], [0.5, 0], [0.5, 1], [0, 1]])

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/templates/vision.html")
def vision():
    return render_template('vision.html')

@app.route("/templates/detection.html")
def stream():
    return render_template('detection.html')

def yolov8_to_detections(yolov8_results, img_size):
    detections = []
    for result in yolov8_results.boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = result
        bbox = [int(x1), int(y1), int(x2), int(y2)]
        detection = {
            "bounding_box": bbox,
            "confidence": conf,
            "class_id": int(cls)
        }
        detections.append(detection)
    return detections

def draw_detections(frame, detections, class_names):
    for detection in detections:
        x1, y1, x2, y2 = detection['bounding_box']
        conf = detection['confidence']
        class_id = detection['class_id']
        
        label = f"{class_names[class_id]} {conf:.2f}"
        color = (0, 255, 0)  # Green color for the bounding box
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def vidstream():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Perform object detection
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = model(frame_rgb, agnostic_nms=True)[0]
            detections = yolov8_to_detections(result, frame.shape[:2])
            
            # Draw detections on the frame
            draw_detections(frame, detections, model.model.names)
            
            # Encode the frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video_stream")
def video_stream():
    return Response(vidstream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

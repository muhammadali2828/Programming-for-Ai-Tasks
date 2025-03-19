from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("yolov8n.pt")  

def generate_frames():
    cam = cv2.VideoCapture(0)

    while True:
        success, img = cam.read()
        if not success:
            break

        output = model(img)

        for detection in output:
            for bbox in detection.boxes:
                x1, y1, x2, y2 = map(int, bbox.xyxy[0])
                confidence = bbox.conf[0]
                category = int(bbox.cls[0])

                if category in [16, 17, 18]:  
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, f"Animal {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cam.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

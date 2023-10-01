from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)


camera = cv2.VideoCapture(0)

@app.route("/")
def home():
  return render_template('home.html')


@app.route("/cam")
def detect():
  return render_template('detection.html')


@app.route("/V15l0N")
def vision():
  return render_template('vision.html')



def vidstream():
  while True:
    success, frame = camera.read()
    if not success:
      break
    else:
      ret, buffer = cv2.imencode('.jpg', frame)
      frame = buffer.tobytes()
      yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' +frame+ b'\r\n')



@app.route("/video_stream")
def video_stream():
  return Response(vidstream(), mimetype='multipart/x-mixed-replace;boundary=frame')




if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, request, Response
import os
import io
import numpy as np
import cv2
from gevent.pywsgi import WSGIServer

import faceblur as f_blur


app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    image = request.files["image"]

    in_memory_file = io.BytesIO()
    image.save(in_memory_file)

    image = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)

    image = f_blur.process_img(image)

    image = cv2.imencode('.jpg',image)[1].tobytes()

    return Response(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n', mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.debug = False
    http_server = WSGIServer((os.environ.get("APP_PORT", default='0.0.0.0'), 5000), app)
    http_server.serve_forever()

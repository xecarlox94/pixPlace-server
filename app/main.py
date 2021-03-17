from flask import Flask, request, Response
import os
from gevent.pywsgi import WSGIServer
import faceblur as f_blur


app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    image = f_blur.proc_req_img(image)

    return Response(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n', mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.debug = False
    http_server = WSGIServer((os.environ.get("APP_PORT", default='0.0.0.0'), 5000), app)
    http_server.serve_forever()

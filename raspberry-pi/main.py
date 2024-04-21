import cv2
from picamera2 import Picamera2
from flask import Flask, Response
import numpy as np
import os
import cloud_pi_lib as CPL
import base64
import json

app = Flask(__name__)

global_response = None

frame_width = 1600
frame_height = 1200

def generate_frames():
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"size": (frame_width, frame_height)}))
    config = picam2.create_preview_configuration({'format': 'RGB888', "size": (frame_width, frame_height)})
    picam2.configure(config)
    picam2.start()

    while True:
    
        frame, response = CPL.camera_function(picam2, 'img_pipe', 'api_pipe.json')


        # Draw the bounding box if there's a response
        if response is not None:
            global_response = response

            # Assuming response structure fits your draw_bounding_box function
            CPL.draw_bounding_box(frame, global_response, frame_width, frame_height)

        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        if not flag:
            continue

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
        

        

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

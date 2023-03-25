from flask import Flask, render_template, request
import cv2
import base64
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def cv2_imread_base64(base64str):
    imgdata = base64.b64decode(base64str)
    image = np.fromstring(imgdata, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


@app.route('/receive', methods=['POST'])
def detect_face():
    encoded_string=request.data[22:]
        
    try:
        img = cv2_imread_base64(encoded_string)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        path = "haarcascade_frontalface_default.xml"

        face_cascade = cv2.CascadeClassifier(path)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
        print(len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        
        ret, buffer = cv2.imencode('.jpg', img)
        base64_image = base64.b64encode(buffer).decode('utf-8') 
        bytes_str = base64_image.encode('utf-8')  # convert the string to bytes
        print(bytes_str[:10])
        img = cv2_imread_base64(bytes_str)
        return bytes_str
    except:
        return encoded_string
    

if __name__ == "__main__":
    app.run(8080)
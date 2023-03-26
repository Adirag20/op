from flask import Flask, render_template, request, jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)

# Rendering our html
@app.route('/')
def index():
    return render_template('index.html')

# convert base64 to cv2 readable format
def cv2_imread_base64(base64str):
    imgdata = base64.b64decode(base64str)
    image = np.fromstring(imgdata, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

# face detection using haar cascade algorithm
def detect_face_opencv(encoded_string):
    try:
        img = cv2_imread_base64(encoded_string)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        path = "haarcascade_frontalface_default.xml" 
        face_cascade = cv2.CascadeClassifier(path)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        (x,y,w,h) = faces[0]
      
        ret, buffer = cv2.imencode('.jpg', img)
        base64_image = base64.b64encode(buffer).decode('utf-8') 
        bytes_str = base64_image.encode('utf-8')  # convert the string to bytes
        return bytes_str
    except:
        return encoded_string

# returning our resultant detected image
@app.route('/receive', methods=['POST'])
def receive():
  url = request.data[22::]
  encoded_string = detect_face_opencv( url)
  encoded_string = 'data:image/jpeg;base64,'+str(encoded_string).split('\'')[1]
  response = jsonify({"image": encoded_string})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response 
      
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
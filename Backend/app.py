from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import base64
import os
import cv2
from json import dumps

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

try:
    os.mkdir('./shots')
except OSError as error:
    pass


@app.route('/')
def index():
  return jsonify({'message':'Server works'})
  
@app.route('/greet')
def say_hello():
  return jsonify({'message':'Greeting from Emmanuel Allan '})

def detect_face(name):
    try:
        os.mkdir(f'./shots/{name}')
    except:
        pass
    # Filename
    filename = f"./shots/{name}/{name}-feed.jpg"
    
    # Reading image from that file
    img = cv2.imread(filename)
    img = cv2.resize(img, (500,500) ) 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # Haarcascade 
    path = "haarcascade_frontalface_default.xml" 
    face_cascade = cv2.CascadeClassifier(path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))

    for(x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    (x,y,w,h) = faces[0]
    # 
    cv2.imwrite(f"./shots/{name}/{name}-face.jpg", img) 
    # cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
    with open(f"./shots/{name}/{name}-face.jpg", "rb") as image_file:
      encoded_string = base64.b64encode(image_file.read())
    return encoded_string

@app.route('/receive/<string:emailId>', methods=['POST'])
def receive(emailId):
  # encoded_string = ""
  if emailId =="undefined":
        return jsonify({'message':'Login to continue'})
      
  emailId = emailId.split("@")[0]
  try:
    os.mkdir(f'./shots/{emailId}')
  except:
    pass
  # url = requests.get(request.data)
  try:
    url = request.data[22::]
    decodedData = base64.b64decode(url + b'==')

    # Write Image from Base64 File
    
    # print("Entered")
    imgFile = open(f'./shots/{emailId}/{emailId}-feed.jpg', 'wb')
    imgFile.write(decodedData)
    imgFile.close()
    # detect_face(emailId)
    
    encoded_string = detect_face(emailId)
    encoded_string = 'data:image/jpeg;base64,'+str(encoded_string).split('\'')[1]
    # print(encoded_string)
    # optional: doing stuff with the data
    # result here: some dict
    # raw_data = {"image": encoded_string}

    # # now: encoding the data to json
    # # result: string
    # json_data = dumps(raw_data, indent=2)
    return jsonify({"image": encoded_string})
      
  except:  
    pass
  print("Received frame", emailId)
  return jsonify({"image":str(encoded_string)})


if __name__ == '__main__':
    #server start port
    app.run(host='0.0.0.0', port=5000)
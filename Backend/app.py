from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import base64
import os
import cv2
from json import dumps
from deepface import DeepFace
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

try:
    os.mkdir('./shots')
except OSError as error:
    pass


@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/greet')
def say_hello():
  return jsonify({'message':'Greeting from Emmanuel Allan '})

  
def cv2_imread_base64_cv(base64str):
    imgdata = base64.b64decode(base64str)
    image = np.fromstring(imgdata, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def detect_face_opencv(name, encoded_string):
    try:
        os.mkdir(f'./shots/{name}')
    except:
        pass
    # Filename
    # filename = f"./shots/{name}/{name}-feed.jpg"
    
    # Reading image from that file
    try:
      img = cv2_imread_base64_cv(encoded_string)
      img = cv2.resize(img, (500,500) ) 
      gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      
      # Haarcascade 
      path = "haarcascade_frontalface_default.xml" 
      face_cascade = cv2.CascadeClassifier(path)
      faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))

      for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
      (x,y,w,h) = faces[0]
      
      ret, buffer = cv2.imencode('.jpg', img)
      base64_image = base64.b64encode(buffer).decode('utf-8') 
      # print(base64_image[:10])
      bytes_str = base64_image.encode('utf-8')  # convert the string to bytes
      return bytes_str
    except:
      print("No face found")
      return encoded_string

  
def cv2_imread_base64_df(base64str):
    imgdata = base64.b64decode(base64str)
    image = np.fromstring(imgdata, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    retval, buffer = cv2.imencode('.jpg', image)
    dataUrl = base64.b64encode(buffer).decode('ascii')
    return dataUrl


  
def detect_face_deepface(name,base64_str):
  try:
    os.mkdir(f'./shots/{name}')
  except:
    pass
  # Filename
  # filename = f"./shots/{name}/{name}-feed.jpg"

  # reading image
  img = cv2_imread_base64_cv(base64_str)
  
  try: 
    image = cv2_imread_base64_df(base64_str)
    obj = DeepFace.analyze(img_path=image, actions=['gender','emotion'])
    
    l = len(obj)
    for i in range(l):
      # getting coordinates of faces
      x = obj[i]['region']['x'] 
      y = obj[i]['region']['y'] 
      w = obj[i]['region']['w'] 
      h = obj[i]['region']['h'] 
      # drawing box around faces
      cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
      
      # getting other details
      gender = "Woman" if obj[i]['gender']['Woman']>=50 else "Man"
      # age = obj[i]['age']
      emotions = obj[i]['emotion']
      emotions_len = len(obj[i]['emotion'])
      
      # Drawing rectangle behind details
      cv2.rectangle(img, (x+w+2,y), (x+w+110,y+160), (0,0,0), -1)
      
      # writing the age, emotion 
      font = cv2.FONT_HERSHEY_SIMPLEX
      fontScale = 0.5
      cv2.putText(img, gender, (x+w+3,y+20), font, fontScale, (0, 255, 0), 1, cv2.LINE_AA)
      # cv2.putText(img, f"Age: {str(age)}", (x+w+3,y+40), font, fontScale, (0, 255, 0), 1, cv2.LINE_AA)
      
      #typing emotions
      count = 50
      emotions = dict(sorted(emotions.items(), key=lambda x: x[1], reverse=True))
      
      for emotion in emotions:
        cv2.putText(img, f"{emotion}:{emotions[emotion].round(2)}", (x+w+3,y+count), font, fontScale, (0, 255, 0), 1, cv2.LINE_AA)
        count+=20
        if(count>150):
            break
          
    # cv2.imwrite(f"./shots/{name}/{name}-face.jpg", img) 
    # # cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
    # with open(f"./shots/{name}/{name}-face.jpg", "rb") as image_file:
    #   encoded_string = base64.b64encode(image_file.read())
    # Read the image in cv2 format
    
    # image = cv2.imread(filename)

    # Convert the image to a byte string
    ret, buffer = cv2.imencode('.jpg', img)
    encoded_string = base64.b64encode(buffer)
      
    return encoded_string
  except:
    ret, buffer = cv2.imencode('.jpg', img)
    encoded_string = base64.b64encode(buffer)
    # print(encoded_string[:10])
    return encoded_string
  


@app.route('/opencv/<string:name>', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def receive(name):
  # encoded_string = ""
  if name =="undefined":
        return jsonify({'message':'Login to continue'})
      
  # name = name.split("@")[0]
  # try:
  #   os.mkdir(f'./shots/{name}')
  # except:
  #   pass
  # url = requests.get(request.data)
  # try:
  url = request.data[22::]
  # decodedData = base64.b64decode(url + b'==')

  # Write Image from Base64 File
  
  # print("Entered")
  # imgFile = open(f'./shots/{name}/{name}-feed.jpg', 'wb')
  # imgFile.write(decodedData)
  # imgFile.close()
  # detect_face(name)
  
  # encoded_string = detect_face_deepface(name, url)
  encoded_string = detect_face_opencv(name, url)
  encoded_string = 'data:image/jpeg;base64,'+str(encoded_string).split('\'')[1]
  # print(encoded_string)
  # optional: doing stuff with the data
  # result here: some dict
  # raw_data = {"image": encoded_string}

  # # now: encoding the data to json
  # # result: string
  # json_data = dumps(raw_data, indent=2)
  response = jsonify({"image": encoded_string})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response 
      
  # except:  
  #   pass
  # print("Received frame", emailId)
  # return jsonify({"image":encoded_string})

# @app.route('/receive/<string:emailId>', methods=['POST'])
# # @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def receive(emailId):
#   # encoded_string = ""
#   if emailId =="undefined":
#         return jsonify({'message':'Login to continue'})
      
#   emailId = emailId.split("@")[0]
#   try:
#     os.mkdir(f'./shots/{emailId}')
#   except:
#     pass
#   # url = requests.get(request.data)
#   # try:
#   url = request.data[22::]
#   decodedData = base64.b64decode(url + b'==')

#   # Write Image from Base64 File
  
#   # print("Entered")
#   imgFile = open(f'./shots/{emailId}/{emailId}-feed.jpg', 'wb')
#   imgFile.write(decodedData)
#   imgFile.close()
#   # detect_face(emailId)
  
#   # encoded_string = detect_face_deepface(emailId, url)
#   encoded_string = detect_face_opencv(emailId, url)
#   encoded_string = 'data:image/jpeg;base64,'+str(encoded_string).split('\'')[1]
#   # print(encoded_string)
#   # optional: doing stuff with the data
#   # result here: some dict
#   # raw_data = {"image": encoded_string}

#   # # now: encoding the data to json
#   # # result: string
#   # json_data = dumps(raw_data, indent=2)
#   response = jsonify({"image": encoded_string})
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   return response 
      
#   # except:  
#   #   pass
#   # print("Received frame", emailId)
#   # return jsonify({"image":encoded_string})


if __name__ == '__main__':
    #server start port
    app.run(host='0.0.0.0', port=5000)
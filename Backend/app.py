from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import base64

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
  return jsonify({'message':'Server works'})
  
@app.route('/greet')
def say_hello():
  return jsonify({'message':'Greeting from Emmanuel Allan '})

@app.route('/receive/<string:emailId>', methods=['POST'])
def receive(emailId):
  if emailId =="undefined":
        return jsonify({'message':'Login to continue'})
      
  emailId = emailId.split("@")[0]
  # url = requests.get(request.data)
  try:
      url = request.data[22::]
      decodedData = base64.b64decode(url + b'==')

      # Write Image from Base64 File
      
      # print("Entered")
      imgFile = open(f'./shots/{emailId}/{emailId}-feed.jpg', 'wb')
      imgFile.write(decodedData)
      imgFile.close()
  except:
      pass
  print("Received frame", emailId)
  return jsonify({'message':'hello hi', "image":str(request.data)})


if __name__ == '__main__':
    #server start port
    app.run(host='0.0.0.0', port=5000)
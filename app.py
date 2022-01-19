from flask import Flask, request
from deepface import DeepFace

app = Flask(__name__)

@app.route('/faceverify',methods = ['POST'])
def home():
	try:
		if (request.method == 'POST'): 
			data = request.get_json()
			result = DeepFace.verify(data['img1'],data['img2'], model_name= "VGG-Face")
			return str(result["verified"])
	except Exception as e:
		return (str(e))

import flask 
from flask import request, jsonify
from deepface import DeepFace
app = flask.Flask(_name_)
app.config["DEBUG"] = True
# passed two images located at the same folder as the .py file 
@app.route('/verify',methods = ['POST'])
def home(): 
	if (request.method == 'POST'): 
		data = request.get_json()
		# print(data)
		result = DeepFace.verify(data['img1'],data['img2'], model_name= "VGG-Face")
		return str(result["verified"])
app.run()
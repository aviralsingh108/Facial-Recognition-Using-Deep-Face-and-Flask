from flask import Flask, request
import os
import json
from face_util import compare_faces

app = Flask(__name__)

@app.route('/face_match', methods=['POST'])
def face_match():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('img1' in request.files) and ('img2' in request.files):        
            file1 = request.files.get('img1')
            file2 = request.files.get('img2')                         
            ret = compare_faces(file1, file2)     
            return ret
                                                    
    
# When debug = True, code is reloaded on the fly while saved
app.run(host='0.0.0.0', port='5001', debug=True)


return str(result["verified"])
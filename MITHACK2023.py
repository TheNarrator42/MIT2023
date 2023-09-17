from flask import Flask, render_template, url_for, request
from distutils.log import debug
from fileinput import filename
import os
import json
import requests

SECRET = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA4ZmU0MDgtMGMyYS00MWYxLTk4NzMtNGIzZjUxYTM3MGUwIiwidHlwZSI6ImFwaV90b2tlbiJ9.SW7Capkzw8nByzrUAz5dWntZ_MUJLK3WpbIHHGVBG40"
headers = {"Authorization": SECRET}

url ="https://api.edenai.run/v2/text/keyword_extraction"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/receive_data', methods=['POST'])
def success():
    textData = request.data.decode('utf-8')
    
    #extract Keywords
    payload={"show_original_response": False,"fallback_providers": "","providers": "amazon,microsoft", "language": "en", "text": textData}
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    result['amazon']['items'] = sorted(result['amazon']['items'], key = lambda x: x["importance"], reverse=True)

    #Create an image based off of the keyword
    userContent = result['amazon']['items'][0]['keyword']    
    input = "\"" + userContent + "\""
    terminalPrompt = "modal run backend/stable_diffusion_cli.py --prompt " + str(input) 
    os.system(terminalPrompt) 


    return(userContent)
    '''
    userContent = request.form['userInput']    
    input = "\'" + userContent + "\'"
    terminalPrompt = "modal run backend/stable_diffusion_cli.py --prompt " + str(input) 
    os.system(terminalPrompt)    
    image_names = os.listdir('static/images')
    return render_template("TxtAck.html", data = userContent, image_names=image_names)
'''
if __name__ == '__main__':
    app.run(debug=True)
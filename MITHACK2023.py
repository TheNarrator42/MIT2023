from flask import Flask, render_template, url_for, request
from distutils.log import debug
from fileinput import filename
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload')
def about():
    return render_template('upload.html')

@app.route('/display', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']   
        f.save(f.filename)
        fileContents = open(f.filename, 'r').read()
        image_names = os.listdir('static/images')
        return render_template("acknowledge.html", name = f.filename, data = fileContents, image_names=image_names)

if __name__ == '__main__':
    app.run(debug=True)
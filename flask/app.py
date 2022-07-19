from crypt import methods
from pydoc import render_doc
import os
from urllib.request import Request
from flask import Flask, render_template, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def index():
    if request.method=='POST':
        file = request.files['file']
       
        # fil = open(file.stream,'r')
        txt=file.stream.read()
        print("hellow this to test")
        print("ehel",txt)
        return render_template('index.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



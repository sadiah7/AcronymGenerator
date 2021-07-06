#! usr/bin/env python3
from flask import Flask,render_template,request
from googlesearch import search

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def getvalue():
    name = request.form['username']
    nam = name
    name = name.split()
    res = ''
    for word in name:
        res += word[0].upper()
    for j in search(nam, num_results=1):
        j = j
    return render_template('pass.html', name=res, link = j)

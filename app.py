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
    for j in search(name, num_results=1):
        link = j
    name = name.split()
    res = ''
    for word in name:
        res += word[0].upper()
    return render_template('pass.html', name=res, link = link)

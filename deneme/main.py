from logging import debug
from typing import IO
import flask
from flask import request,jsonify
import requests,json

app=flask.Flask(__name__)

rqst=requests.get('https://jsonplaceholder.typicode.com/posts')
dizi=rqst.json()

@app.route("/said")
def home():
    dgr=request.args.get('dgr',type=str,default='')
    if (dgr=='1'): return 'Merhaba'
    return jsonify(dizi[int(dgr)])


app.run(debug=True)





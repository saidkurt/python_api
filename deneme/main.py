from logging import debug
from typing import IO
import flask
from flask import request,jsonify
import requests,json

app=flask.Flask(__name__)

rqst=requests.get('https://jsonplaceholder.typicode.com/posts')
dizi=rqst.json()

@app.route('/said',methods=['GET'])
def home():
    dgr=request.args.get('dgr',type=int,default='')
    prs=request.args.get('prs',type=int,default='')
    
    if (dgr==1 and prs==2): return 'Merhaba'
    return jsonify(dizi[dgr+prs])

@app.route('/mehmet/ahmet',methods=['GET'])
def sss():
    dgr=request.args.get('dgr',type=int,default='')
    prs=request.args.get('prs',type=int,default='')
    
    if (dgr==1 and prs==2): return 'Merhaba'
    return jsonify(dizi[dgr+prs])


app.run(debug=True)


#http://127.0.0.1:5000/said?dgr=1

#Merhaba

#http://127.0.0.1:5000/said?dgr=2

#{
#  "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
#  "id": 3,
#  "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
#  "userId": 1
#}
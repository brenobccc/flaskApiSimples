import os
import requests
from flask import Flask, request, jsonify, json 

app = Flask(__name__)

@app.route("/primeira/<nome>")
def ok(nome):
	return "Nome:"+nome

app.run(host="0.0.0.0", port = 2000, debug = False)
